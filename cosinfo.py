def main() :
    user_menu = input("검색을 하고 싶으면 1번, 성분을 저장하고 싶으면 2번을 누르시오 : ")
    if user_menu == "2":
        name = input("성분 이름을 입력하세요: ")
    
        # 성분 정보 입력 받기
        function = input("이 성분의 기능을 입력하세요: ")
        safety = input("이 성분의 ph는 얼마인가요?: ")
        safety_int = int(safety)
        safety_str = ""
        common_in = input("주로 사용되는 제품을 입력하세요: ")

        if 3 <= safety_int and safety_int < 4:
            safety_str = "주의 필요"

        if 4 <= safety_int and safety_int < 5:
            safety_str = "매우 안전함"
                        
        if 5 <= safety_int and safety_int < 7:
            safety_str = "보통"

        if 7 <= safety_int and safety_int <= 9:
            safety_str = "위험할 수 있음"

        hello=open(name,"w")

        hello.write("-기능: " + function + "\n")  # 뒤 \n은 줄 바꿈을 위해
        hello.write("-ph: " + safety + "\n")
        hello.write("-안전성: " + safety_str + "\n")
        hello.write("-주 사용 제품: " + common_in + "\n")

        hello.close()

        print(f"{name} 성분이 등록되었습니다.")
       
    elif user_menu == "1":
        sourcename=input("검색할 성분명을 입력하시오: ")
        file = open(sourcename,"r")
        content = file.read()
        print(content)
        file.close()

    # 반복
    main()
    

main()
