


'''
 새로 가입하는 유저들이 카카오 아이디 규칙에 맞지 않는 아이디를 입력했을 때,
 입력된 아이디와 유사하면서 규칙에 맞는 아이디를 추천해주는 프로그램을 개발하는 것입니다.

    - 아이디의 길이는 3자 이상 15자 이하여야 합니다.
    - 아이디는 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 문자만 사용할 수 있습니다.
    - 단, 마침표(.)는 처음과 끝에 사용할 수 없으며 또한 연속으로 사용할 수 없습니다.

    신규 id가 new_id일 경우

    1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
    2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
    3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
        만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
    7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.


    즉,
    1단계 : 대문자 -> 소문자 변경
    2단계 : 소문자,숫자, -, _, . 제외 모든 문제 제거
    3단계 : .. -> . 로 치환
    4단계 : .이 처음이나 끝에 위치하면 제거
    5단계 : 빈문자열 일때 a를 넣어줌
    6단계 : 16자 이상 -> 15개 제외 다 없애기 그리고 마지막이 .일 경우 . 제거
    7단계 : 2글자 이하라면, 마지막 문자를 3자가 될 때까지 반복

'''

def solution(new_id):

    # 1단계
    new_id = new_id.lower()

    # 2단계
    for i in new_id:



    answer = ''
    return answer


new_id = "...!@BaT#*..y.abcdefghijklm"

print(solution(new_id))