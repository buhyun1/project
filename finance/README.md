## AWS 리눅스 환경 카카오 pororo 모델<br> 사용 요약 및 긍,부정 뉴스 기사 선별

## ec2 anaconda 설치 및 pororo 설치, 실행 과정

1. sudo apt-get update 
2. wget https://repo.anaconda.com/archive/Anaconda3-2022.05-Linux-x86_64.sh (ubuntu 폴더에서 작업할 것)
3. bash Anaconda3-2022.05-Linux-x86_64.sh (설치 완료되면 reload)
4. conda create -n pororo python=3.7 (가상환경 설치)
5. conda install pytorch==1.6.0 torchvision==0.7.0 cudatoolkit=10.1 -c pytorch (가상환경 버전 맞추기)
6. git clone https://github.com/kakaobrain/pororo.git
7. cd pororo
8. pip install -e . (pororo 설치)
9. conda activate /opt/conda/envs/pororo (폴더 이동 가상환경 실행)
10. python /home/ubuntu/pororo/batch.py (코드 실행)
11. conda deactivate (가상환경 종료)

## 가상환경 버전
python = 3.7.0 <br>
pytorch = 1.6.0 설치 후 최신 업데이트 <br>
pororo = 0.4.1 <br>