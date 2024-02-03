import os
import openai
import customtkinter as ctk


def generate():
    prompt = 'Please generate 10 ideas for coding projects.'
    # Requested language type
    language = language_dropdown.get()
    prompt += 'The programming language is ' + language + '.'

    # Requested difficulty level
    difficulty = difficulty_level.get()
    prompt += 'The difficulty is ' + difficulty + '.'

    if checkbox1.get():
        prompt += 'The the project should include a database. '
    if checkbox1.get():
        prompt += 'The the project should include an API. '

    print(prompt)
    openai.api_key = os.getenv("OPENAI_API_KEY")

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=2000,
        n=1,
        stop=None,
        temperature=0.5,
    )

    answer = response.choices[0].text.strip()
    print(answer)
    result_textbox.insert('0.0',answer)



root = ctk.CTk()
root.geometry("750x700")
root.title('ChatGPT project idea Generator')
ctk.set_appearance_mode('dark')

# title label
title_lbl = ctk.CTkLabel(root,text='Project Idea Generator',
                         font=ctk.CTkFont(size=40,weight='bold'))
title_lbl.pack(padx=10,pady=(40,30))


# frame1
frame = ctk.CTkFrame(root)
frame.pack(fill='x',padx=100)


# frame 1-1
language_frame = ctk.CTkFrame(frame)
language_frame.pack(padx=100,pady=10,fill='both')
# language label in frame 0-1
language_lbl = ctk.CTkLabel(language_frame,text='Programming language',
                            font=ctk.CTkFont(size=20))
language_lbl.pack()
# select language with ComboBox
language_dropdown = ctk.CTkComboBox(language_frame,
                                    values=['python','javascript','java'])
language_dropdown.pack(pady=10)


# frame 1-2
difficulty_frame = ctk.CTkFrame(frame)
difficulty_frame.pack(padx=100,pady=10,fill='both')
# difficulty label in frame 1-2
difficulty_lbl = ctk.CTkLabel(difficulty_frame,text='Project difficulty',
                            font=ctk.CTkFont(size=20))
difficulty_lbl.pack()
# Difficulty levels with RadioBottun
difficulty_level = ctk.StringVar(value='Easy')
# first RadioButton
radiobutton1 = ctk.CTkRadioButton(
    difficulty_frame,text='Easy', variable = difficulty_level ,value = 'Easy')
radiobutton1.pack(side='left',padx=(20,10),pady=10)
# second RadioButton
radiobutton2 = ctk.CTkRadioButton(
    difficulty_frame,text='Medium' , variable = difficulty_level , value = 'Medium')
radiobutton2.pack(side='left',padx=10,pady=10)
# third RadioButton
radiobutton3 = ctk.CTkRadioButton(
    difficulty_frame,text='Hard', variable = difficulty_level , value = 'Hard')
radiobutton3.pack(side='left',padx=10,pady=10)



# frame 1-3
features_frame = ctk.CTkFrame(frame)
features_frame.pack(padx=100,pady=10,fill='both')
# features label in frame 1-2
features_lbl = ctk.CTkLabel(features_frame,text='Features',
                            font=ctk.CTkFont(size=20))
features_lbl.pack()
# Select features with checkbox
# Firis checkBox
checkbox1 = ctk.CTkCheckBox(features_frame,text='DataBase')
checkbox1.pack(side='left',padx=50,pady=10)
# Second checkBox
checkbox2 = ctk.CTkCheckBox(features_frame,text='API')
checkbox2.pack(side='left',padx=50,pady=10)

# button
Generate_btn = ctk.CTkButton(frame,text='Generate Ideas',command=generate)
Generate_btn.pack(padx=100,fill='x',pady=10)


# result --> show with textbox
result_textbox = ctk.CTkTextbox(root,font=ctk.CTkFont(size=15)) 
result_textbox.pack(pady=10,fill='x',padx=100)

root.mainloop()