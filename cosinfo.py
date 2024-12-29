# 성분 데이터 저장용 딕셔너리
ingredient_info = {}

print("검색을 하고 싶으면 1번, 성분을 저장하고 싶으면 2번을 누르시오")
if input()==2:

# 성분 정보 등록 함수
    def register_ingredient():
        name = input("성분 이름을 입력하세요: ")
    

    
    # 성분 정보 입력 받기
        sourcename = input("이 성분의 기능을 입력하세요: ")
        safety = input("이 성분의 ph는 얼마인가요?: ")
        common_in = input("주로 사용되는 제품을 입력하세요: ")

        hello=open(sourcename,"w")
        hello.write{sourcename ==input("이 성분의 기능을 입력하세요: ")}
             safety = input("이 성분의 ph는 얼마인가요?: ")
                    if 4<=int(input())<5:
                        hello.write("매우 안전함")
                        
                    if 3<=int(input())<4:
                        hello.write("주의 필요")
                    if 5<=int(input()<7):
                        hello.write("보통")
                    if 7<=int(input()<=9):
                        hello.write("위험할 수 있음")
                    
                    
             hello.write{input("주로 사용되는 제품을 입력하세요: ")
                }


       print(f"{name} 성분이 등록되었습니다.")
elif input()==1:
    sourcename=input("검색할 성분명을 입력하시오:")
    open(sourcename,"r")


main()
