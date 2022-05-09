import wget
import content

for index in range(0,211):
    data = content.info(index)
    print(data['music'])
    try:
        url1 = str(data['music'])
        filename = wget.download(url1)
    except:
        print('err')