pipenv install
pipenv lock -r
pip3 install -r requirements.txt
xvfb-run -a /path/to/orca "$@"
chmod +x run.sh
pipenv run ./run.sh &
./run.sh &
