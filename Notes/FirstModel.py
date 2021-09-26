#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def tanit_es_kiertekel(df,model,bemeno_valtozok):
    ismert_df = df[  df['past_or_future']=="past" ] 
    train_df, test_df = train_test_split(ismert_df, random_state=42, test_size=0.3)
    model.fit(train_df[bemeno_valtozok],train_df[celvaltozo])
    test_df=test_df.copy()
    test_df['p0']=0
    test_df['p1']=0
    test_df[['p0','p1']] = model.predict_proba(test_df[bemeno_valtozok])
    def profit(x):
        if x==1:
            return 15000
        else:
            return -100000
    test_df['profit_az_adott_ugyfelen']=test_df[celvaltozo].apply(profit)
    x_tengely=[]
    y_tengely=[]

    for szazalek in range(0,101,1):
        limit = szazalek /100.0
        hitelezettek = test_df[   test_df['p1']>=limit  ]
        osszprofit = hitelezettek['profit_az_adott_ugyfelen'].sum()
        x_tengely.append(szazalek)
        y_tengely.append(osszprofit)
    
    for i in range(0,len(y_tengely),1):
        if y_tengely[i]==np.max(y_tengely):
            limit_valoszinuseg=x_tengely[i]/100
    
    egy_fore_profit=np.max(y_tengely)/len(test_df)
    return len(jovo)*egy_fore_profit,limit_valoszinuseg
    
bemeno_valtozok=['Nyugdij_ertek','Sex_F','Age','PERSONAL_NET_INCOME','MATE_INCOME']
model=DecisionTreeClassifier(max_depth=3,random_state=42)
tanit_es_kiertekel(df,model,bemeno_valtozok)

