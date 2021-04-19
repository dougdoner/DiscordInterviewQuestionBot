FROM gorialis/discord.py

WORKDIR ./

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "example_bot.py"]