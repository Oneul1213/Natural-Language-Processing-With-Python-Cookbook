# 2장 처리 전 텍스트, 소싱, 정규화 - RSS 피드에서 내용 읽기
import feedparser


# 피드 가져오기
myFeed = feedparser.parse("http://feeds.mashable.com/Mashable")

# 피드 제목, 현재 피드에 있는 게시물 수 출력
print('피드 제목 :', myFeed['feed']['title'])
print('포스트 수 :', len(myFeed.entries))

# 첫 번째 post의 제목 출력
post = myFeed.entries[0]
print('포스트 제목 :', post.title)

# HTML 콘텐츠에 액세스하기
content = post.content[0].value
print('콘텐츠 원본 :\n', content)
