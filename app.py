from sre_parse import expand_template
import streamlit as st
import torch
from transformers import T5Tokenizer, AutoModelForCausalLM,GPT2LMHeadModel

#cacheの定義
def cached_tokenizer(tokenizer_name):
    tokenizer = T5Tokenizer.from_pretrained(f'rinna/japanese-{tokenizer_name}')
    tokenizer.do_lower_case = True
    return tokenizer

def cached_model_small(model_name):
    model = GPT2LMHeadModel.from_pretrained(f'rinna/japanese-{model_name}')
    return model

def cached_model(model_name):
    model = AutoModelForCausalLM.from_pretrained(f'rinna/japanese-{model_name}')
    return model

def main():
  st.title('Sentence Generator')

  #モデルの選択
  with st.expander('set model'):
    selected_model = st.selectbox('使用したいモデルを選択してください。',
                                  ['gpt2-small','gpt2-medium','gpt-1b'])
    
    st.caption('各モデルを初めて使用する場合は処理にしばらく時間がかかります。')
    st.caption('gpt-1bを使用する場合はGPUが搭載されているPCでの実行を推奨します。')

  #パラメータの設定
  with st.expander('set parameter'):
    temperature_value = st.slider(label='ランダム度',
                    min_value=0.0,
                    max_value=1.0,
                    value=0.9,
                    )

    top_k_value = st.slider(label='top_k',
                    min_value=0,
                    max_value=100,
                    value=40,
                    )

    top_p_value = st.slider(label='top_p',
                    min_value=0.0,
                    max_value=1.0,
                    value=1.0,
                    )                   

    penalty_value = st.slider(label='繰り返しに対するペナルティ',
                    min_value=0.0,
                    max_value=1.0,
                    value=0.95,
                    )

    length_value = st.slider(label='出力する最大文字数',
                    min_value=30,
                    max_value=500,
                    value=100,
                    )

    st.write('各パラメータについて')
    tab1,tab2,tab3,tab4,tab5 = st.tabs(['ランダム度','top_k','top_p','繰り返しに対するペナルティ','出力する最大文字数'])

    with tab1:
      st.caption('出力のランダムさを調整します。（推奨　0.7～1.0）')
      st.caption('ランダム度とtop_pはどちらかを固定してもう一方を変更することを推奨します。')
    with tab2:
      st.caption('出力する際の語彙の幅を調整します。')  
      st.caption('値を大きくすると、より多くの語彙を出力の候補とします。') 
    with tab3:
      st.caption('出力する際の語彙の幅を調整します。')
      st.caption('値を大きくすると、関連度の高い語彙が出力されやすくなります。')
      st.caption('ランダム度とtop_pはどちらかを固定してもう一方を変更することを推奨します。')
    with tab4:
      st.caption('同じ文が繰り返し出力される場合は値を大きくして下さい。')
      st.caption('0.9以下に設定すると、同じ文が生成されやすくなります。') 
    with tab5:
      st.caption('出力する最大文字数を設定することができます。長いほど処理に時間がかかります。')
      st.caption('処理に時間がかかりすぎている場合は、短くしてみてください。')

  PREFIX_TEXT = st.text_area(
        label='テキスト入力', 
        value='吾輩は猫である。'
  )
  st.caption('5～6文ほど入力するとより良い出力が期待できます。')

  progress_num = 0
  status_text = st.empty()
  progress_bar = st.progress(progress_num)

  #文章の生成機能
  if st.button('文章生成'):
    if st.button('キャンセル'):
      st.stop()
    st.text('処理を中断したい場合はキャンセルボタンを押してください。')

    progress_num = 10
    status_text.text(f'Progress: {progress_num}%')
    progress_bar.progress(progress_num)

    #tokenizerのロード
    tokenizer = cached_tokenizer(selected_model)
    
    progress_num = 30
    status_text.text(f'Progress: {progress_num}%')
    progress_bar.progress(progress_num)

    #modelのロード
    if selected_model=="gpt2-small":
      model = cached_model_small(selected_model) 

    else:
      model = cached_model(selected_model) 

    progress_num = 50
    status_text.text(f'Progress: {progress_num}%')
    progress_bar.progress(progress_num)

    input = tokenizer.encode(PREFIX_TEXT, return_tensors="pt") 
    progress_num = 70
    status_text.text(f'Progress: {progress_num}%')
    progress_bar.progress(progress_num)

    #文章の生成
    output = model.generate(
            input, do_sample=True, 
            temperature=temperature_value,
            max_length=length_value,
            top_k=top_k_value,
            top_p=top_p_value,
            repetition_penalty=penalty_value,            
            )

    progress_num = 90
    status_text.text(f'Progress: {progress_num}%')
    progress_bar.progress(progress_num)

    #特定文字の削除
    output_text = "".join(tokenizer.batch_decode(output)).replace("</s>", "")
    output_text = output_text.replace("<unk>", "")
    output_text = output_text.replace("</unk>", "")
    output_text = output_text.replace("[UNK]", "")

    progress_num = 95
    status_text.text(f'Progress: {progress_num}%')
    progress_bar.progress(progress_num)

    #結果の表示
    st.info('生成結果')
    progress_num = 100
    status_text.text(f'Progress: {progress_num}%')
    st.write(output_text)
    progress_bar.progress(progress_num)

if __name__ == '__main__':
  main()