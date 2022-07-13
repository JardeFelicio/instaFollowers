#from datetime import datetime
import instaloader
from PyQt5 import  uic,QtWidgets

app=QtWidgets.QApplication([])
tela=uic.loadUi("notFollow.ui")


seguindo_list=[]
seguidores_list=[]
difere=[]

def userAccount():
    conta=tela.lineEdit_user.text()

def instaFollow():
    #Carrega a lib e faz login com a conta desejada
    L = instaloader.Instaloader()
    L.login('lulu_sousaff', '85029639')




    conta=tela.lineEdit_user.text()
    #conta=input("Qual o @ que vc deseja analisar?\n")

    #Carrega o perfil escolhido
    try:
        profile = instaloader.Profile.from_username(L.context, conta)
    except:
        print("Falha no Login")

    # lista de seguidores
    seguidores_list = []
    count=0
    for followee in profile.get_followers():
        print("Carregando -- Seguidores..."+str((count+1)))
        seguidores_list.append(followee.username)
        file = open("seguidores"+conta+".txt","a+")
        file.write(seguidores_list[count])
        file.write("\n")
        file.close()
        #print(followers_list[count])
        count=count+1

    # lista de seguindo
    seguindo_list = []
    count=0
    for followee in profile.get_followees():
        print("Carregando -- Seguindo..."+str((count+1)))
        seguindo_list.append(followee.username)
        file = open("seguindo"+conta+".txt","a+")
        file.write(seguindo_list[count])
        file.write("\n")
        file.close()
        #print(followees_list[count])
        count=count+1

    # lista de não segue de volta
    difere = list(set(seguindo_list).difference(seguidores_list))

    count=0
    for var in difere:
        print("Carregando -- Não Segue de Volta...")
        file = open("list_difere"+conta+".txt","a+")
        file.writelines(str(var)+'\n')
        file.close()

    print("\n\nResultado:\n")
    print('Seguindo:'+str(len(seguindo_list))+'\n')
    print('Seguidores:'+str(len(seguidores_list))+'\n')
    print('Não segue de volta:'+str(len(difere))+'\n' )

tela.btnEnviar.clicked.connect(instaFollow)

tela.show()
app.exec()




