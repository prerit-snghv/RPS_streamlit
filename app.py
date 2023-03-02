#Modules used
import streamlit as st
import cv2
import random
from PIL import Image as im
import matplotlib.pyplot as plt
from Classify import teachable_machine_classification

#Page Config
st.set_page_config(
    page_title='Rock Paper Scissors Shoot',
    layout="centered",
    initial_sidebar_state="auto",
    menu_items=None)

x=st.sidebar.radio('Navigation',['Instruction','Game','Data','Leader Board'])

if 'Name' not in st.session_state:
    st.session_state.Name = 'XYZ'

def instruction():
    st.title('Stone Paper Scissors Game')
    st.session_state.Name=st.text_input('Enter your name: ',placeholder='...')
    st.info('Play the classic game of ROCK PAPER SCISSORS')
    st.write('Remember the rules:')
    st.write('Rock smashes Scissor')
    st.write('Scissor cuts Paper')
    st.write('Paper captures Rock')
    st.write('Please use the following postures to play your move:')
    col1,col2,col3=st.columns(3)
    with col1:
        st.write('Keep in mind the following posture for Rock')
        st.image('P_rock.jpg')
    with col2:
        st.write('Keep in mind the following posture for Paper')
        st.image('P_paper.jpg')
    with col3:
        st.write('Keep in mind the following posture for Scissor')
        st.image('P_scissor.jpg')
    

def game():
    #initializing values
    if 'score' not in st.session_state:
        st.session_state.score = 0

    if 'y' not in st.session_state:
        st.session_state.y=None

    if 'r' not in st.session_state:
        st.session_state.r = 0
        
    if 'p' not in st.session_state:
        st.session_state.p = 0
        
    if 's' not in st.session_state:
        st.session_state.s = 0

    if 'win' not in st.session_state:
        st.session_state.win = 0

    if 'lose' not in st.session_state:
        st.session_state.lose = 0

    if 'draw' not in st.session_state:
        st.session_state.draw = 0
    
    if 'res' not in st.session_state:
        st.session_state.res = None
    
    if 'run' not in st.session_state:
        st.session_state.run=0
    

    #Screen
    st.title('Stone Paper Scissors Game')
    col1, col2, col3 = st.columns([3,2,3])

    #algorithm and scoring
    def algo_scoring(x):
     
        #Algorithm

        def Compplays(List):
            choices={0:1,1:2,2:0}
            if st.session_state.y==None:
                st.session_state.y=1
            else:
                if st.session_state.res=='Lose':
                    st.session_state.y=choices.get(List[-1])
                elif st.session_state.res=='Draw':
                    st.session_state.y=random.randint(0,2)
                elif st.session_state.res=='Win':
                    st.session_state.y=choices.get(st.session_state.y)
            st.session_state.run+=1
            return st.session_state.y
        sc = sh = d = 0

        List=[]
        List.append(x)
        st.session_state.y=Compplays(List)

        if st.session_state.y==0:
            play='Rock'
        elif st.session_state.y==1:
            play='Paper'
        elif st.session_state.y==2:
            play='Scissor'
        with col3:
            st.image(play+'.png',width=224)
            st.write('Computer plays',play)
        
        #Scoring
        if play == 'Rock':
            if x == 1:
                with col2:
                    st.success('You win this round!')
                sh += 1
                st.session_state.p += 1
                st.session_state.score+=10
                st.session_state.win+=1
                st.session_state.res='Lose'
            elif x == 0:
                with col2:
                    st.warning('It\'s a draw!')
                st.session_state.r += 1
                d += 1
                st.session_state.score=st.session_state.score
                st.session_state.draw+=1
                st.session_state.res='Draw'
            else:
                with col2:
                    st.error('You lose this round!')
                st.session_state.s += 1
                sc += 1
                st.session_state.score-=10
                st.session_state.lose+=1
                st.session_state.res='Win'
            
        elif play == 'Paper':
            if x == 1:
                with col2:
                    st.warning('It\'s a draw!')
                st.session_state.p += 1
                d += 1
                st.session_state.score=st.session_state.score
                st.session_state.draw+=1
                st.session_state.res='Draw'
            elif x == 0:
                with col2:
                    st.error('You lose this round!')
                st.session_state.r += 1
                sc += 1
                st.session_state.score-=10
                st.session_state.lose+=1
                st.session_state.res='Win'
            else:
                with col2:
                    st.success('You win this round!')
                st.session_state.s += 1
                sh += 1
                st.session_state.score+=10
                st.session_state.win+=1
                st.session_state.res='Lose'

        else:
            if x == 1:
                with col2:
                    st.error('You lose this round!')
                st.session_state.p += 1
                sc += 1
                st.session_state.score-=10
                st.session_state.lose+=1
                st.session_state.res='Win'
            elif x == 0:
                with col2:
                    st.success('You win this round!')
                st.session_state.r += 1
                sh += 1
                st.session_state.score+=10
                st.session_state.win+=1
                st.session_state.res='Lose'
            else:
                with col2:
                    st.warning('It\'s a draw!')
                st.session_state.s += 1
                d += 1
                st.session_state.score=st.session_state.score
                st.session_state.draw+=1
                st.session_state.res='Draw'
        

    
    #Working
    with col2:
        st.header('Score')

    with col3:
        st.header('Computer')

    with col1:
        
        st.header(st.session_state.Name)
        
        #Initializing camera
        check = st.button("Cam On")
        save = st.button("Save")
        camera = cv2.VideoCapture(0)
        Cam1 = st.image([])
        Cam2 = st.image([])
        
        while check:
            
            #Switching camera
            return_value,image = camera.read()
            img2 = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
            img3 = cv2.flip(img2,1)
            Cam1.image(img3)
        
        if save:
            
            #Image capture
            a,image = camera.read()
            im2 = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
            im3 = cv2.flip(im2,1)
            Cam2.image(im3)
            plt.imsave('P_img.jpeg', im3)
            new = im.open(r"C:\Users\prsin\OneDrive\Documents\python_files\Streamlit\P_img.jpeg")
            size = (224,224)
            new.resize(size)
            
            #Choice
            opts={0:'Stone',1:'Paper',2:'Scissor'}
            player = teachable_machine_classification(new)
            
            #Algorithm and scoring
            algo_scoring(player)
            
            #Score display
            st.write(st.session_state.Name,'plays',opts.get(player))
            with col2:
                st.info(st.session_state.score)
        camera.release()
        
def graph():
    st.title('Stone Paper Scissors Game')
    col1, col2, col3 = st.columns(3)
    col1.metric("Rock", value=st.session_state.r)
    col2.metric("Paper", value=st.session_state.p)
    col3.metric("Scissor", value=st.session_state.s)
    labels = ['Win','Lose','Draw']
    size = [st.session_state.win,st.session_state.lose,st.session_state.draw]
    fig1, ax1 = plt.subplots()
    ax1.pie(size, labels=labels, explode = (0.05,0.05,0.05), autopct='%1.1f%%',shadow=True, startangle=90)
    ax1.axis('equal')
    st.pyplot(fig1)

import mysql.connector as c
def results(name, score):
    con = c.connect(host = 'localhost', user = 'root', password = 'LRSP', database = 'Leader')
    cur = con.cursor()
    s0 = 'Select * from leaderboard where Name=(%s);'
    cur.execute(s0,(name,))
    x=cur.fetchall()
    if len(x)>0:
        s1= 'UPDATE leaderboard SET High_Score=(%s) WHERE Name=(%s);'
        cur.execute(s1, (score,name))
    else:
        s2 = 'insert into leaderboard values(%s, %s);'
        cur.execute(s2, (name, score))
        con.commit()
        
    @st.experimental_memo(ttl=600)
    def run_query(query):
        with con.cursor() as cur:
            cur.execute(query)
            return cur.fetchall()

    rows = run_query("SELECT * from leaderboard ORDER BY High_Score Desc;")

    st.write(f"Name:Score")
    for row in rows:
        st.write(f"{row[0]}:{row[1]}")

def options(x):
    if x=='Instruction':
        instruction()
    elif x=='Game':
        game()
    elif x=='Data':
        graph()
    elif x=='Leader Board':
        results(st.session_state.Name,st.session_state.score)

options(x)