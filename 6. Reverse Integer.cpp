class Solution {
public:
    int reverse(int x) {
        
        long int ans=0,l,flag=0,limit;
        int n;
        
        limit=pow(2,30)*2;
        
        if(x<0)
        {
            flag=1;
            x=x*(-1);
        }
        
        n=l=(int)log10(x)+1;
        
        //cout<<n;
        
        for(int i=0;i<l;i++)
        {
            long int temp=pow(10,n-1);
            ans=ans+pow(10,i)*(int)(x/temp);
            x=x%temp;
            n--;
        }
        
        
        if(ans<limit*(-1) || ans>limit-1)
            return 0;
        else if(flag==1)
            return ans*(-1);
        else
            return ans;
        
    }
};