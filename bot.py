<!DOCTYPE html>
<html lang="ar">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>GigaEarn MiniApp</title>
  <script src="https://telegram.org/js/telegram-web-app.js"></script>
  <!-- سكربت GigaEarn: ضع هنا الـ PROJECT ID الخاص بك -->
  <script src="https://ad.gigapub.tech/script?id=1801"></script>
  <style>
    body {
      font-family: sans-serif;
      text-align: center;
      background: #f9f9f9;
      padding: 30px;
    }
    button {
      background: #0088cc;
      color: white;
      padding: 15px 25px;
      font-size: 18px;
      border: none;
      border-radius: 12px;
      cursor: pointer;
    }
    button:disabled {
      background: gray;
      cursor: not-allowed;
    }
  </style>
</head>
<body>
  <h2>🎁 شاهد إعلان واربح نقاط</h2>
  <button id="watchAd">▶️ شاهد الإعلان</button>

  <script>
    const tg = window.Telegram.WebApp;
    tg.expand(); // فتح الميني آب بكامل الشاشة

    const watchBtn = document.getElementById("watchAd");

    watchBtn.addEventListener("click", async () => {
      watchBtn.disabled = true;
      try {
        // عرض الإعلان من GigaEarn
        await window.showGiga();

        // إرسال المكافأة + ID للمستخدم للبوت
        tg.sendData(JSON.stringify({ user_id: 1801, reward: 10 }));

        alert("✅ مبروك! حصلت على 10 نقاط");
      } catch (err) {
        console.error("خطأ أثناء عرض الإعلان:", err);
        alert("⚠️ فشل عرض الإعلان. حاول مرة ثانية");
      } finally {
        watchBtn.disabled = false;
      }
    });
  </script>
</body>
</html>