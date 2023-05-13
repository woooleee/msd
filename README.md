
# MSD
<br/>
📆 2023.04 ~ 
<br>

## Explanation
This is code repository for geospatial data preprocessing

## Codes



```python
from mod import *
seoulsicheong = (126.9784147, 37.5666805) # 서울특별시청
busansicheong = (129.0756416, 35.1795543) # 부산광역시청
samsungsds    = (127.1004553, 37.5163278) # 삼성 SDS
test1 = '부산광역시 부산진구 범천동 862-1' # ABL 부산타워
test2 = '서울시 강남구 논현로 508' # GS 강남타워

print('---------test---------')
# 서울특별시청 중점 반지름 1000미터 원 내의 지하철역 개수
print(FacilityCnt('metro', seoulsicheong, 1000)) # 9
# 삼성SDS 중점 반지름 1000미터 원 내의 지하철역 개수
print(FacilityCnt('metro', samsungsds, 1000)) # 4 
# 서울특별시청에서 가장 가까운 지하철역의 거리(미터))
print(NearestFacilityDist('metro', seoulsicheong)) # 161.03723884981463
# 삼성SDS에서 가장 가까운 지하철역의 거리(미터))
print(NearestFacilityDist('metro', samsungsds)) # 208.25857850466434
# 서울특별시청 중점 반지름 500미터 원 내의 스타벅스 개수
print(FacilityCnt('starbucks', seoulsicheong, 500)) # 16
# 서울특별시청 중점 반지름 1000미터 원 내의 블루보틀 개수
print(FacilityCnt('bluebottle', seoulsicheong, 1000)) # 2
# 부산시청 중점 반지름 3000미터 원 내의 블루보틀 개수
print(FacilityCnt('bluebottle', busansicheong, 3000)) # 0
# ABL 부산타워 좌표(경도, 위도)
print(AddrToCoord(test1))  # 129.059656, 35.1497815
# GS 강남타워 지번 주소
print(CoordToAddr((127.0373364, 37.5019949), '지번')) # 서울특별시 강남구 역삼동 679-1
# GS 강남타워 도로명 주소
print(CoordToAddr((127.0373364, 37.5019949), '도로명'))  # 서울특별시 강남구 논현로 508
# ABL 부산타워 도로명 주소
print(CoordToAddr((129.059656, 35.1497815), '도로명'))  # 부산광역시 부산진구 중앙대로 640

```

## Status

Preparing data for feature extraction



## Repository Structure

```text
- msd(root)
  - asset
    - postprocess
    - preprocess
    - rawfile
  - experiment
  - preprocess
    - constant.py
    - building_bd.ipynb
    - business_corp.ipynb
    - people_metro.ipynb
    - people_popse.ipynb
  - security
    - security.yaml
  - util
    - distance.py
    - epsg_transform.py
    - get_coord_vw.py
    - get_coord.py
    - nfd_to_nfc.py
  - README.md
  - requirements.xtx
  - docs
```

## Features
| Title              | Author         | Link      | Loc
|--------------------|----------------|-----------|-----  |
|--------------------|----------------|-----------|-----  |
|--------------------|----------------|-----------|-----  |
|--------------------|----------------|-----------|-----  |
|--------------------|----------------|-----------|-----  |
|--------------------|----------------|-----------|-----  |
|--------------------|----------------|-----------|-----  |

<!-- 
ADM_SECT_C,idx,pnu,rlgcd,linm,bun,ji,naroadcd,namainbun,nasubbun,x,y,platarea,archarea,bcrat,totarea,vlrat,heit,grndflrcnt,ugrndflrcnt,rideuseelvtcnt,emgenuseelvtcnt,useaprday,2019,2020,2021,2022,x_5179,y_5179,index_right,geometry_grids -->

## Dataset Origin

| Title              | Author         | Link      | Loc
|--------------------|----------------|-----------|-----  |
|--------------------|----------------|-----------|-----  |
|--------------------|----------------|-----------|-----  |
|--------------------|----------------|-----------|-----  |
|--------------------|----------------|-----------|-----  |
|--------------------|----------------|-----------|-----  |
|--------------------|----------------|-----------|-----  |