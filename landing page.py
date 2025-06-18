<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>SmartLearn - Landing Page</title>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      font-family: 'Poppins', sans-serif;
      background: linear-gradient(to right, #4facfe, #00f2fe);
      color: white;
      text-align: center;
      padding: 40px 20px;
      transition: background 0.5s ease;
    }

    header {
      animation: fadeIn 1s ease-in;
    }

    h1 {
      font-size: 3rem;
      margin-bottom: 10px;
    }

    p {
      font-size: 1.2rem;
      margin-bottom: 30px;
      max-width: 600px;
      margin-left: auto;
      margin-right: auto;
    }

    .cta-button {
      padding: 15px 30px;
      font-size: 1rem;
      font-weight: 600;
      color: white;
      background-color: #ff4b2b;
      border: none;
      border-radius: 30px;
      cursor: pointer;
      transition: transform 0.3s ease, background 0.3s ease;
    }

    .cta-button:hover {
      transform: scale(1.1);
      background-color: #ff416c;
    }

    footer {
      margin-top: 60px;
      font-size: 0.9rem;
      opacity: 0.8;
    }

    @keyframes fadeIn {
      0% { opacity: 0; transform: translateY(-30px); }
      100% { opacity: 1; transform: translateY(0); }
    }
  </style>
</head>
<body>
  <header>
    <h1>SmartLearn</h1>
    <p>Master new skills with our online courses. Learn at your own pace with video lessons, quizzes, and live support.</p>
    <button class="cta-button" onclick="subscribe()">Get Started</button>
  </header>

  <footer>
    © 2025 SmartLearn. All rights reserved.
  </footer>

  <script>
    function subscribe() {
      alert("🎉 Welcome to SmartLearn! We'll get you started.");
      document.body.style.background = 'linear-gradient(to right, #ff758c, #ff7eb3)';
    }
  </script>
</body>
</html>

