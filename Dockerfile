# Python 3.9-slim ইমেজ ব্যবহার করা হচ্ছে
FROM python:3.9-slim

# কন্টেইনারের ভেতরে /app নামে একটি ওয়ার্কডিরেক্টরি তৈরি করা হচ্ছে
WORKDIR /app

# requirements.txt ফাইলটি কপি করা হচ্ছে
COPY requirements.txt .

# প্যাকেজ ইনস্টল করার কমান্ড
RUN pip install --no-cache-dir -r requirements.txt

# মূল প্রোজেক্ট ফাইলগুলি কপি করা হচ্ছে
COPY . .

# uvicorn কমান্ডের মাধ্যমে FastAPI সার্ভার চালু করা হচ্ছে
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
