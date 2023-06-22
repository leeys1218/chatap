<style>
    @keyframes appear {
      from {
        opacity: 0;
      }
      to {
        opacity: 1;
      }
    }

    body {
      background-image: url("./public/images/background.jpg");
      background-size: cover;
      height: 100vh;
      color: white;
    }
    .container {
      animation: appear 2s ease;
      animation-fill-mode: forwards;
      opacity: 0;

      max-width: 800px;
      margin: 0 auto;
      padding: 40px;
      background-color: lightgray;
      background-color: rgba( 255, 255, 255, 0.5 );

      border-radius: 8px;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
  
    h1 {
      font-size: 24px;
      font-weight: bold;
      margin-bottom: 20px;
      color: #333333;
    }

    pre {
      white-space: pre-wrap;
      font-size: 20px;
      color: #333333;
    }
  

  </style>
  
  <script>
  
  let data = localStorage.getItem("answer");
  data = JSON.parse(data)
  data.replace('\n', '<br>')
  data.replace('\n\n', '<br>')
  
  </script>
  
  <body>
    <div class="container">
      <h1>Psychologist Answers</h1>
      <pre>{data}</pre>
    </div>
  </body>


