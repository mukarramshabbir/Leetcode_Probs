class SnapshotArray(object):
    def __init__(self,length):
        self.array={}
        self.snap_id=0
    
    def set(self,index,val):
        if index not in self.array:
            self.array[index]=[]
        self.array[index].append((self.snap_id,val))
        
    def snap(self):
        self.snap_id+=1
        return self.snap_id-1
    
    def get(self, index, snap_id):
        if index in self.array:
            snapshots=self.array[index]
            left,right=0,len(snapshots)-1
            while left<=right:
                mid=(left+right)//2
                if snapshots[mid][0]<=snap_id:
                    left=mid+1
                else:
                    right=mid-1
            if right>=0:
                return snapshots[right][1]
        return 0

    
if __name__=="__main__":
    s = "ab"
    goal = "ab"
    res=buddyStrings(s,goal)
    print(res)