import random

play = True        #再戦判断を持つ変数
date = [ 0,0,0,0,] #戦歴をもつリスト[プレイ回数,勝ち,負け,引き分け]


#「再戦のループ」#
while play :
    date[0] += 1 
    turn = True    #自分のターン継続するかのループ
    result = False #結果を持つ変数
    
    print("\n============ブラックジャック=============")

    myhand=[]   #自分の手札作成
    pairhand=[] #相手の手札作成

    #両者、最初に配られるカード（2枚）手札に加える
    for x in range(2):
        myhand.append(random.randint(1,10))
        pairhand.append(random.randint(1,10))


    #「相手の動作」#
    while sum(pairhand) <= 16 and len(pairhand) < 5:
        pairhand.append(random.randint(1,10))
    #「相手の動作」ここまで#


    #「自分の動作」#
    while turn :
        
        input_error = True  #入力値が適切か判断する変数
        
        print("\nあなたの手札:" , myhand)
        print("現在の合計　:" , sum(myhand))

        #カードを引ける状態か判断
        if sum(myhand) < 21 and len(myhand) < 5:
            print("\n「　カードを引きますか？　」(１か２を入力)")
            print("　├１：はい　　→　カードを引く")
            print("　└２：いいえ　→　勝負")

            #「入力の確認処理」#
            while input_error :
                input_num = input()#入力値取得
                if not input_num.isdigit() :
                    print("１か２を入力してください")
                    continue
                input_num = int(input_num)
                if input_num == 1 or input_num == 2 :
                    input_error = False
                else:
                    print("１か２を入力してください")
            #「入力の確認処理」ここまで#
            
            if input_num == 1 :
                myhand.append(random.randint(1,10))
            else :
                turn = False
            print("\n========================================")
        else :
            break
    #「自分の動作」ここまで#


    #「結果発表」#
    

    if (
        sum(myhand) == sum(pairhand) or
        (sum(myhand) > 21 and sum(pairhand) > 21)
    ):
        print("\n________________引き分け________________")
        date[3] += 1
        
    else:
        if sum(myhand) <= 21 :
            if (
                (sum(myhand) <= 21 and sum(pairhand) > 21) or
                (sum(myhand) == 21 and sum(pairhand) != 21) or
                (sum(myhand) > sum(pairhand) and sum(pairhand) != 21)
            ):          
                result = True
            
        if result :
                
             print("\n__________________勝利__________________")
             date[1] += 1
        else:
            print("\n__________________敗北__________________")
            date[2] += 1
            
    print("\n合計：" , sum(myhand),"あなたの手札:" , myhand)
    print("合計：" , sum(pairhand),"相手の手札　:" , pairhand)
    print("________________________________________")
    #「結果発表」ここまで#
            
    print("\n\n=================戦歴===================")
    print(f"           {date[0]}戦　{date[1]}勝　{date[2]}敗　{date[3]}分")
    print("========================================")
    
    #「再戦の判断」#
    print("\n「　再戦しますか？　」(１か２を入力)")
    print("　├１：はい　　→　再プレイ")
    print("　└２：いいえ　→　終了　")

    input_error = True

    #「入力の確認処理」#
    while input_error :
        input_num = input()
        if not input_num.isdigit() :
            print("１か２を入力してください")
            continue
        input_num = int(input_num)
        if input_num == 1 or input_num == 2 :
            input_error = False
        else:
            print("１か２を入力してください")
    #「入力の確認処理」ここまで#
    
    if input_num == 2 :
        play = False
    #「再戦の判断」ここまで#

        
#「再戦のループ」ここまで#
        
print("\n終了しました")
