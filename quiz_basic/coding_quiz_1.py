names = ['유튜버1','유튜버2','유튜버3','유튜버4']

'''
이것은 주석

'''
for name in names:
    with open(f"{name}.txt", 'w', encoding='utf-8') as f:
        f.write(f'안녕하세요? {name}님.\n\n')
        f.write('현재 저희 출판사는 파아썬에 관한 주제로 책 출간을 기획 중입니다.\n')
        f.write(f'{name}님의 유튜브 영상을 보고 연락을 드리게 되었습니다.\n')
        f.write('자세한 내용은 첨부드리는 제안서를 확인 ㅣ부탁드리며, 긍정적인 회신 기다리겠습니다.\n\n')
        f.write('좋은 하루 보내세요 ^^\n')
        f.write('감사합니다.')