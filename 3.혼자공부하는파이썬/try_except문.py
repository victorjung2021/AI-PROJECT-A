#변수선언
list_input_a= ["52","254","43","46","스파이","102"] 
#반복적용
list_number =[]
for item in list_input_a:
    #숫자로 변환해서 리스트에 추가
    try:
        float(item) #예외발생시 알아서 다음으로 진행안됨
        list_number.append(item) #예외없이 통과되면 리스트에 추가
    except:
        pass
print("{}내부에 있는 숫자는", format(list_input_a))
print("{}입니다".format(list_number)) 


try:
    #예외가 발생할 수 있는 가능성이 있는 코드
    print(float(input(">숫자를 입력해 주세요 : ")) ** 2)
    
except:
    #예외가 발생했을때 실행할 
    print("잘못입력되었습니다.")

    