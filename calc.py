import numpy as np
import matrixoperations as mp
matriz = []
matrizcomposta = []
matrizpontossrc = []
matrizsrusrc = []
matrizSrcSrp = []
matrizjp = []
matrizpontossrt = []
vrp = []
p = []
n = []
faces = []
arestas = []


nimput = int(input("Numero de vertices:"))

for i in range(nimput):
    x, y, z, n = input("Vertice:").split()
    matriz += [[float(x),float(y),float(z),float(n)]]

matriz = np.array(matriz).T;
print(matriz)
inp = -1
pmatriz = matriz
while (inp!=0):
    print("\n--------------------------\n")
    print(" Imprimir matriz Atual(1)\n Rotacao(2)\n Translacao(3)\n Scala(4)\n Cizalhamento(5)")
    print(" Centro Geometrico(6)\n Converter SRU Para SRC(7)")
    print(" Converter SRC Para SRP(8)\n Gerar Matriz Composta(9)")
    print(" Gerar Matriz Composta SRU Para SRT(10)\n Gerando Matriz de pontos de SRU Para SRT(11)")

    inp = int(input("Digite a opcao:"))

    if inp == 1:
         print("\n-------Matriz Atual-------\n")
         print(pmatriz)

    elif inp == 2 :
        graus = float(input())
        eixo = input()
        matrizRotacao,pmatriz = mp.rotacao(pmatriz, graus,eixo)
        pmatriz = np.round(pmatriz,3) 
        print("\n-------Matriz Rotacionada-------\n")
        print(pmatriz)
        if(input("Armazenar para a compsta?")=='s'):
            matrizcomposta.insert(0,matrizRotacao)

    elif inp == 3:
        matriztranslacao = []
        verticea = np.array(input("Digite as coordenadas x,y e z, do vertice a ser transladado:").split()).astype(float)
        verticeb = np.array(input("Digite as coordenadas x,y e z, do ponto de destino do vertice :").split()).astype(float)
        matriztranslacao, pmatriz = mp.translacao(pmatriz,verticea,verticeb)
        pmatriz = np.round(pmatriz,3)
        print("\n-------Matriz Translada-------\n")
        print(pmatriz)
        if(input("Armazenar para a compsta?")=='s'):
            matrizcomposta.insert(0,matriztranslacao)

    elif inp == 4:
        matrizscala =[]
        vertice = np.array(input("Digite o fator de escala para x,y e z:").split()).astype(float)
        matrizscala, pmatriz = mp.scala(pmatriz,vertice)
        pmatriz = np.round(pmatriz,3)
        print("\n-------Matriz Scalada-------\n")
        print(pmatriz)
        if(input("Armazenar para a compsta?")=='s'):
            matrizcomposta.insert(0,matrizscala)

    elif inp == 5:
        vertice = np.array(input("Digite o fator de cizalhamento para x e y:").split()).astype(float)
        matrizcilhamento, pmatriz = mp.cizalhamento(pmatriz,vertice)
        print("\n-------Matriz Cizalhada-------\n")
        print(pmatriz)
        if(input("Armazenar para a compsta?")=='s'):
            matrizcomposta.insert(0,matrizcilhamento)

    elif inp == 6:        
        print("\n-------Centro Geometrico-------\n")
        mp.centrogeometrico(pmatriz)
    
    elif inp == 7:
        print("\n-------SRU -> SRC-------\n")
        vrp = np.array(input("VRP:").split()).astype(float)
        p = np.array(input("P:").split()).astype(float)        
        
        print("\n-------Matriz Translacao-------\n")
        mT = mp.MatrizT(vrp)

        print("\n-------Calculo vetor n^-------\n")        
        vn = mp.vetorN(vrp,p)

        print("\n-------Calculo vetor v^-------\n")
        vvu = np.array(input("Vetor View Up:").split()).astype(float)        
        vv = mp.vetorV(vn,vvu)

        print("\n-------Calculo vetor u^-------\n")
        vu = mp.vetorU(vv,vn)

        print("\n-------Matriz R-------\n")
        mR = mp.matrizR(vu,vv,vn)

        print("\n-------Matriz SRU,SRC-------\n")
        matrizsrusrc = mp.MsruMsrc(mR,mT)
        matrizsrusrc = np.round(matrizsrusrc,3)
        print("MsruMsrc\n",matrizsrusrc)        
        ##for v in matrizsrusrc:
          ##  print(np.round(v,3))
        print("\n-------Matriz de pontos Multiplicada-------\n")
        matrizpontossrc = np.round(np.dot(matrizsrusrc,pmatriz),3)
        nvrp=np.round(np.dot(matrizsrusrc,np.append(vrp,1).T),3)
        print(matrizpontossrc)
        print("VRP=",nvrp)

    elif inp == 8:
        print("\n-------SRC -> SRP-------\n")
        dp = float(input("dp:"))
        matrizSrcSrp, pmatriz = mp.matrizProjecaoPers(matrizpontossrc,dp)
        print("\n-------Matriz janela projecao-------\n")
        dx = np.array(input("x min, x max: ").split()).astype(float)
        dy = np.array(input("y min, y max: ").split()).astype(float)
        du = np.array(input("u min, u max: ").split()).astype(float)
        dv = np.array(input("v min, v max: ").split()).astype(float)
        matrizjp = np.round(mp.matrizjp(dx,dy,du,dv),3)     

    elif inp == 9:
        print("\n-------Matriz composta-------\n")
        mcomposta = matrizcomposta.pop(0)
        print(np.round(mcomposta,3),"\n")
        for m in matrizcomposta:
            mcomposta = np.dot(mcomposta,m)
            print(np.round(m,3),"\n")
            print(np.round(mcomposta,3),"\n\n")
        print(np.round(mcomposta,3))
    elif inp == 10:
        print("\n-------Gerando Matriz Composta SRU Para SRT-------\n")
        print("Matriz Projecao\n",matrizjp,"\n")
        print("Matriz SRCSRP\n",matrizSrcSrp,"\n")
        print("Matriz SRUSRC\n",matrizsrusrc,"\n")
        mcomposta = np.dot(matrizjp,matrizSrcSrp)
        mcomposta = np.dot(mcomposta,matrizsrusrc)
        print("Matriz Composta SRUSRT\n",np.round(mcomposta,3))

    elif inp == 11:
        print("\n-------Gerando Matriz de pontos de SRU Para SRT-------\n")
        matrizpontossrt = np.round(np.dot(mcomposta,matriz),3)
        print(matrizpontossrt)
        matrizpontossrt[0] = matrizpontossrt[0]/matrizpontossrt[3]
        matrizpontossrt[1] = matrizpontossrt[1]/matrizpontossrt[3]
        matrizpontossrt[3] = matrizpontossrt[3]/matrizpontossrt[3]
        print("\n-------Pontos Normalizados-------\n")
        print(np.round(matrizpontossrt,3)) 
    
    elif inp == 12:
        print("\n-------Multiplicacao Matriz Composta pela de pontos-------\n")
        print (np.round((np.dot(mcomposta,matriz)),3))

    elif inp == 13:
        arestas = []
        print(pmatriz)
        nimput = int(input("Numero de faces:"))
        mimput = int(input("Numero de arestas:"))
        for i in range(nimput):
            start,end = input("aresta:").split()
            estart = [
                matriz[0][start],
                matriz[1][start],
                matriz[2][start],
                matriz[3][start]
            ]
            eend = [
                matriz[0][end],
                matriz[1][end],
                matriz[2][end],
                matriz[3][end]
            ]
            arestas += [[estart],[eend]]       
        