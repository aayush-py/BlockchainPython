import time 
import hashlib

#BlockIndex=0
vChain=[]

class Block:
    
    def __init__(self, nIndex, sData):
        self.__nIndex=nIndex
        self.__nNonce=-1
        self.__sData=sData
        self.__tTime=time.mktime(time.localtime())
        self.__sHash=""
        self.sPreviousHash=""
    
    def GetHash(self):
        return self.__sHash
    
    def MineBlock(self,nDifficulty):
        cstr=[]
        for i in range(nDifficulty):
            cstr.append('0')
        cstr="".join(cstr)
        while(self.__sHash[:nDifficulty]!='0'*nDifficulty):
            print("Mining...", self.__CalculateHash())
            self.__nNonce+=1
            self.__sHash=self.__CalculateHash()
        
        print("Block mined: ",self.__sHash)
    
    def __CalculateHash(self):
        ss=str(self.__nIndex)+str(self.__tTime)+str(self.__sData)+str(self.__nNonce)+str(self.sPreviousHash)
        return hashlib.sha256(ss.encode(encoding='utf-8')).hexdigest()
    
class Blockchain:
    
    def __init__(self):
        self.__nDifficulty=2
        self.vChain=vChain.append(Block(0,"First Block"))
    
    def AddBlock(self,bNew):#pass only blocks
        bNew.sPreviousHash = Blockchain.GetLastBlock().GetHash()
        bNew.MineBlock(self.__nDifficulty)
        vChain.append(bNew)    
        
    def GetLastBlock():
        return vChain[len(vChain)-1]
        #returns a block   
        
bChain = Blockchain()

print("Mining Block...")
bChain.AddBlock(Block(1,"Apple"))        
bChain.AddBlock(Block(2,"Banana"))
