String = '''심예린	Leah	1D1	jsa40450@naver.com
정시후	Daniel	1A3	vid102@hanmail.net
손범석	Jeffy	2A6	sbssbs2006@naver.com'''.split('\n')

base = '''Gospeaking 온라인 학습 정보
{} {}                                 반명: {}
아이디: {}     패스워드: 0509
접속주소: new.gospeaking.com

고스피킹은 핸드폰, PC 둘다 학습이 가능하며
크롬 브라우저에서 원활히 학습 가능합니다.
(고스피킹 과제를 하기 위해선 헤드셋이 필요합니다.)
'''

for line in String:
    a,b,c,d = line.split()
    print(base.format(a,b,c,d))

