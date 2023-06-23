<script>
    import { push } from 'svelte-spa-router';
    import fastapi from "../lib/api";

    let isLoading = false;

    function post_question(mbti, content) {
        let url = "/api/question/create"
        let params = {
            mbti: mbti,
            content: content,
        }

        isLoading = true;
        let _url = import.meta.env.VITE_SERVER_URL+url

        
        fastapi('post', url, params, 
            (json) => {
              localStorage.setItem("answer", JSON.stringify(json)); 
              push("/answer");
            },
            (json_error) => {
                error = json_error
            }
        )
    }
  
    function handleClick(event) {
      const mbtiOption = event.currentTarget;
      const mbtiRow = mbtiOption.parentNode;
  
      const buttons = mbtiRow.querySelectorAll('.mbti-option');
      buttons.forEach((button) => {
        button.style.backgroundColor = '';
        button.classList.remove('selected');
      });
  
      mbtiOption.style.backgroundColor = "#CCCCCC";
      mbtiOption.classList.add('selected');
    }
  
    function handleSubmit() {
      
      const selectedButtons = document.querySelectorAll('.mbti-option.selected');
      const content = document.getElementById('input').value
      
      let mbti = "";
      selectedButtons.forEach((button) => {
        mbti += button.value;
      });
      console.log(mbti)
      console.log(content)
      post_question(mbti, content)
    }
  
  </script>


{#if isLoading}
<body>
  <div> 성격 유형과 질문을 분석중입니다...</div>
</body>
{:else}
<body>
  <div class="container">
    <div class="hero">
      <h1>Tell your worry</h1>
      <p>MBTI를 선택하고, 상황과 감정을 자세히 묘사하세요</p>
    </div>
  
    <div class="mbti-container">
  
      <div class="mbti-row">
        <button class="mbti-option" value="I" on:click={handleClick}>
          <div class="mbti-text">I</div>
          <div class="mbti-description">Introverted</div>
        </button>
        <button class="mbti-option" value="E" on:click={handleClick}>
          <div class="mbti-text">E</div>
          <div class="mbti-description">Extraverted</div>
        </button>
      </div>
  
      <div class="mbti-row">
        <button class="mbti-option" value="N" on:click={handleClick}>
          <div class="mbti-text">N</div>
          <div class="mbti-description">Intuitive</div>
        </button>
        <button class="mbti-option" value="S" on:click={handleClick}>
          <div class="mbti-text">S</div>
          <div class="mbti-description">Sensing</div>
        </button>
      </div>
  
      <div class="mbti-row">
        <button class="mbti-option" value="T" on:click={handleClick}>
          <div class="mbti-text">T</div>
          <div class="mbti-description">Thinking</div>
        </button>
        <button class="mbti-option" value="F" on:click={handleClick}>
          <div class="mbti-text">F</div>
          <div class="mbti-description">Feeling</div>
        </button>
      </div>
  
      <div class="mbti-row">
        <button class="mbti-option" value="J" on:click={handleClick}>
          <div class="mbti-text">J</div>
          <div class="mbti-description">Judging</div>
        </button>
        <button class="mbti-option" value="P" on:click={handleClick}>
          <div class="mbti-text">P</div>
          <div class="mbti-description">Perceiving</div>
        </button>
      </div>
    </div>
  
    <div class="input-container">
      <label for="input">What's on your mind?</label>
      <textarea id="input" name="input" rows="6" placeholder="여기에 내용을 입력하세요,,,"></textarea>
      <button class="submit-button" on:click={handleSubmit}>보내기</button>
    </div>
  </div>
  </body>
{/if}



  
  
  <style>
  
  @keyframes appear {
    from {
      opacity: 0;
    }
    to {
      opacity: 1;
    }
  }
  
  @media (min-width: 768px) {
    .container {
      padding-left: 20%;
      padding-right: 20%;
    }
  }
  
  body {
    background-image: url('./images/background.jpg');
    background-size: cover;
    height: 100vh;
    color: white;
  }
  
  .hero, .mbti-container, .input-container {
    animation: appear 3s ease;
    animation-fill-mode: forwards;
    opacity: 0;
  }
  
  .hero {
    padding: 10px;
    padding-bottom: 10px;
    padding-top: 80px;
    text-align: center;
  }
  
  h1 {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 15px;
  }
  
  p {
    font-size: 16px;
    margin-bottom: 20px;
  }
  
  .input-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    opacity: 0.9;
  }
  
  label {
    font-size: 16px;
    margin-bottom: 5px;
  }
  
  textarea {
    text-align: center;
    width: 90%;
    padding: 10px;
    font-size: 20px;
    border-radius: 20px;
    border: none;
    box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.2);
    margin-bottom: 15px;
    resize: vertical;
    max-height: 200px;
    opacity: 0.5;
  }
  
  .submit-button {
    color: white;
    opacity: 0.7;
    width: 90%;
    padding: 10px;
    font-size: 20px;
    border-radius: 20px;
    border: none;
    box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.6);
    background-color: rgba(0, 0, 0, 0);
  }
  
  .submit-button:hover {
      transform: scale(1.1);
      transition: transform 0.2s ease;
    }
  
  .mbti-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    margin-bottom: 30px;
  }
  
  .mbti-row {
    margin: 0 auto;
    padding: 10px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    margin-bottom: 20px;
  }
  
  .mbti-option {
    flex-basis: calc(50% - 10px);
    padding: 20px;
    cursor: pointer;
    display: flex;
    align-items: center;
    flex-direction: column;
    color: white;
    background-color: rgba(0,0,0,0);
    border:none;
  }
  
  .mbti-option:hover {
    background-color: #CCCCCC;
  }
  
  .mbti-option.selected {
    background-color: #CCCCCC;
  }
  
  .mbti-text {
    font-size: 30px;
    font-weight: bold;
  }
  
  .mbti-description {
    font-size: 12px;
  }
  
  @media only screen and (max-width: 768px) {
    body {
      height: 768px;
    }
  
    .mbti-option {
      flex-basis: calc(50% - 5px);
      padding: 10px;
    }
    
    .mbti-text {
      font-size: 24px;
    }
    
    .mbti-description {
      font-size: 10px;
    }
    
    .mbti-row {
      padding: 5px;
      margin-bottom: 10px;
    }
  }
  
  </style>