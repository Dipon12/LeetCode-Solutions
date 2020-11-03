class Solution {
public:
    
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        
        int sum,carry=0,a,b;
        struct ListNode* l3=NULL; 
        struct ListNode* head=NULL;
        struct ListNode* newNode=NULL;
        
        l3=(struct ListNode*)malloc(sizeof(struct ListNode));
        
        
        
        
        while(l1!=NULL || l2!=NULL || carry==1 )
        {
            if(l1!=NULL)
            {
                a=l1->val;
                l1=l1->next;
            }
            else
            {
                a=0;
                l1==NULL;
            }
                
            
            if(l2!=NULL)
            {
                b=l2->val;
                l2=l2->next;
            }
            else
            {
                b=0;
                l2==NULL;
            }
            sum=a+b+carry;
            carry=0;
            
            
            if(sum>9)
            {
                sum=sum-10;
                carry=1;
            }
         
            
            newNode=(struct ListNode *)malloc(sizeof(struct ListNode));
            
            newNode->next=NULL;
            newNode->val=sum;
            
            if(head==NULL)
                l3=head=newNode;
            else
            {
                l3->next=newNode;
                l3=newNode;
            }
                
            cout<<sum<<endl;
            
            
            
        }
        
        return head;
        
        
    }
};