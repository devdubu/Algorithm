'''

1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
     만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.

'''
import re
def solution(new_id):
    last_char =''
    # 문자열 길이 측정
    id_len_first = len(new_id)

    #소문자로 변환
    new_id = new_id.lower()
    print(new_id)
    #-,_,., 소문자, 숫자 제외 모든 문자 제거
    new_id = re.sub(r"[^a-zA-Z0-9.\-_]","",new_id)
    print(new_id)
    # .이 연속으로 있으면 .으로 모두 치환
    new_id = re.sub('(([.])\\2{1,})', '.', new_id)  # 연속된 같은 문자 변환 (2개이상)
    print(new_id)
    #.가 처음, 끝에 위치하면 제거
    new_id = new_id.strip('.')
    print(new_id)
    # 빈 문자열이면, a를 대입(만약 모든 문자가 제거되었울 때, 처음 제거된 문자열만큼 추가)
    # 문자열 길이가 16자 이상이면 모두 제거(if 제거 후 마침표가 있다면 그것도 제거)
    id_len_second = len(new_id)
    if len(new_id) == 0:
        for i in range(id_len_first):
            new_id += 'a'
    elif id_len_second >= 16:
        new_id = new_id[:15]
        new_id = new_id.strip('.')
    elif id_len_second <= 2: # 길이가 2이하라면, 마지막 문자를 길이가 3이되게 반복하기
        last_char = new_id.strip()[-1]
        while len(new_id) < 3:
            new_id += last_char

    answer = new_id
    return answer

new_id = 'abcdefghijklmn.p'
ans = solution(new_id)
print(ans)