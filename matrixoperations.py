import numpy as np
import math
np.set_printoptions(suppress=True)

from numpy.core.records import array

def rotacao(matriz, angulo, eixo):
    sen = math.sin(math.radians(angulo))
    cos = math.cos(math.radians(angulo))
    ##print(sen, cos)
    matrizres = matriz    
    matrizrotacao = []
    print("\n-------Matriz de Rotacao-------\n")
    if eixo == 'x':
        matrizrotacao = np.array( [
            [1.0, 0.0, 0.0, 0.0],
            [0.0, cos, -(sen), 0.0],
            [0.0, sen, cos, 0.0],
            [0.0, 0.0, 0.0, 1.0]
        ])        
        matrizres = np.dot(matrizrotacao,matriz)
        print(np.round(matrizrotacao,3))

    elif eixo == 'y':
        matrizrotacao = np.array( [
            [cos, 0.0, sen, 0.0],
            [0.0, 1.0, 0.0, 0.0],
            [-(sen), 0.0, cos, 0.0],
            [0.0, 0.0, 0.0, 1.0]
        ])        
        matrizres = np.dot(matrizrotacao,matriz)
        print(np.round(matrizrotacao,3))

    elif eixo == 'z':
        matrizrotacao = np.array( [            
            [cos, -(sen), 0.0, 0.0],
            [sen, cos, 0.0, 0.0],
            [0.0, 0.0, 1.0, 0.0],
            [0.0, 0.0, 0.0, 1.0]
        ])        
        matrizres = np.dot(matrizrotacao,matriz)
        print(np.round(matrizrotacao,3))
    return matrizrotacao,matrizres

def translacao(matriz, verticea, verticeb):
    print("\n-------Matriz de Translacao-------\n")
    matriztranslacao = np.array([
        [1.0, 0.0, 0.0,  verticeb[0] - verticea[0]],
        [0.0, 1.0, 0.0, verticeb[1] - verticea[1]],
        [0.0, 0.0, 1.0, verticeb[2] - verticea[2]],
        [0.0, 0.0, 0.0, 1.0]
    ])
    print(np.round(matriztranslacao,3))
    return (matriztranslacao, np.dot(matriztranslacao,matriz))

def scala(matriz, vertice):
    print("\n-------Matriz de Scala-------\n")
    matrizsacala = np.array([
        [vertice[0], 0.0, 0.0, 0.0],
        [0.0, vertice[1], 0.0, 0.0],
        [0.0, 0.0, vertice[2], 0.0],
        [0.0, 0.0, 0.0, 1.0]
    ])    
    print(np.round(matrizsacala,3))
    return (matrizsacala, np.round(np.dot(matrizsacala,matriz),3))

def cizalhamento(matriz,xy):
    print("\n-------Matriz de Cizalhamento-------\n")
    matrizcizalhamento = np.array([
        [1.0, xy[0], 0.0, 0.0],
        [xy[1], 1.0, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0]
    ]).astype(float)
    print(np.round(matrizcizalhamento,3))
    return (matrizcizalhamento,np.dot(matrizcizalhamento,matriz))

def centrogeometrico(matriz):
    dx = [matriz[0][0],matriz[0][0]]
    dy = [matriz[1][0],matriz[1][0]]
    dz = [matriz[2][0],matriz[2][0]]
    for v in matriz.T:
        if v[0]<dx[0] : dx[0]=v[0]

        elif v[0]>dx[1] : dx[1]=v[0]

        if v[1]<dy[0] : dy[0]=v[1]

        elif v[1]>dy[1] : dy[1]=v[1]

        if v[2]<dz[0] : dz[0]=v[2]

        elif v[2]>dz[1] : dz[1]=v[2]
    print("x=(",dx[0]," + ", dx[1],")/2")
    print("y=(",dy[0]," + ", dy[1],")/2")
    print("z=(",dz[0]," + ", dz[1],")/2")
    print(np.array([(dx[0] + dx[1])/2,(dy[0]+dy[1])/2,(dz[0]+dz[1])/2]))

def vetorN(vrp,p):    
    N = vrp - p    
    print("N->",N)
    cN = np.round(math.sqrt((pow(N[0],2)+pow(N[1],2)+pow(N[2],2))),3)
    print("|N|=sqrt(pow(",N[0],",2)+pow(",N[1],",2)+pow(",N[2],",2)",")")
    print("|N|=",cN)
    vn = np.round(np.array([
        N[0]/cN,
        N[1]/cN,
        N[2]/cN,
    ]),3)
    print("n^=",N,"/",cN)
    print("n^=",vn)
    return vn

def vetorV(vn, vvu):
    print("V->=",vvu," - ", "(","(",vvu,"*",vn,")","*",vn,")")
    print("V->=",vvu," - ","(",np.round(np.dot(vvu,vn),3),"*",vn,")")
    print("V->=",vvu," - ",np.round(np.dot(vvu,vn)*vn),3)
    print("V->=",np.round(vvu - np.dot(vvu,vn)*vn),3)
    sv = np.round(vvu - np.dot(vvu,vn)*vn,3)
    cv = np.round(math.sqrt((pow(sv[0],2)+pow(sv[1],2)+pow(sv[2],2))),3)
    print("|V| = ",cv)
    print("v^=",sv,"/",cv)
    vv = np.round(sv/cv,3)
    print("v^=",vv)
    return vv

def vetorU(vv,vn):
    vu=np.round(np.cross(vv,vn),3)
    print("u^=",vv,"X",vn,"\nu^=",vu)
    return vu

def matrizR(vu,vv,vn):
    mR = np.array([
        np.append(vu,0.0),
        np.append(vv,0.0),
        np.append(vn,0.0),
        [0,0,0,1]
    ]).astype(float)
    print(mR)
    return mR

def MatrizT(vrp):
    TranslacaoVrpP = np.array([
        [1.0, 0.0, 0.0, -(vrp[0])],
        [0.0, 1.0, 0.0, -(vrp[1])],
        [0.0, 0.0, 1.0, -(vrp[2])],
        [0.0, 0.0, 0.0, 1.0],
    ]).astype(float)
    print(TranslacaoVrpP)
    return TranslacaoVrpP

def MsruMsrc(matrizR, matrizT):
    print("Matriz R * Matriz T")
    return np.array(np.dot(matrizR,matrizT))

## dp é distancia entre o plano de projeção e o centro de projeção ou origem/vrp
def matrizProjecaoPers(matrizSRC,dp):
    mpers = np.array([
        [1.0 , 0.0, 0.0, 0.0],
        [0.0 , 1.0, 0.0, 0.0],
        [0.0 , 0.0, 1.0, 0.0],
        [0.0 , 0.0, -(1/dp), 0.0],
    ]).astype(float)
    print("\n-------Matriz Projecao-------\n")    
    print(mpers)    
    print("\n-------Pontos Projetados-------\n")    
    mPontoPers = np.round(np.dot(mpers,matrizSRC),3)
    print(mPontoPers)
    vetaux = mPontoPers[3]
    mPontoPers = np.round((mPontoPers/vetaux),3)
    print("\n-------Pontos Normalizados-------\n")    
    print(mPontoPers)
    return (mpers, mPontoPers)

def matrizjp(dx,dy,du,dv):
    deltau = du[1]-du[0]
    deltax = dx[1]-dx[0]
    deltay = dy[1]-dy[0]
    deltav = dv[1]-dv[0]
    
    mjp = np.array([
        [deltau/deltax, 0.0, 0.0, -(dx[0])*(deltau/deltax)+du[0]],
        [0.0, (dv[0]-dv[1])/deltay, 0.0, dy[0]*(deltav/deltay)+dv[1]],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0]
    ]).astype(float)
    mjp = np.round(mjp,3);
    print(mjp)
    return (mjp)

def z_edge(edge):
    init, end = edge[0], edge[1]
    if(init[1]>end[1]):
        init, end = edge[1], edge[0]    
    dx, dy, dz = end[0]-init[0], end[1]-init[1], end[2]-init[2]
    return dx/dy, dz/dy


def z_edges(edges):
    zedges = []
    for edge in range(len(edges)):
        zedges.append(z_edge(edge))        
        
