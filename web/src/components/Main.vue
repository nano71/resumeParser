<template>
  <div id="main">
    <div class="content">
      <div class="topTitle">
        渐进式简历解析系统
      </div>
      <div class="uploadContent">
        <div class="inputBox">
          <input class="input" type="file"/>
        </div>
        <div class="iconBox">
          <img src="../assets/file.png" alt="">
        </div>
        <div class="textBox">
          <div>点击 或 拖拽</div>
          <div>即可上传简历文件</div>
        </div>
      </div>
      <div class="parserButton">
        <div class="button">开始解析</div>
      </div>
    </div>
  </div>
</template>

<style lang="less" scoped>
img {
  width: 100%;
  height: 100%;
}

#main {
  //width: 100vw;
  //height: 100vh;
  display: flex;
  justify-content: center;
  align-content: center;
}

.content {
  min-width: 200px;

  .topTitle {
    font-size: 50px;
    font-weight: bolder;
    color: #000000;
    margin-bottom: 40px;
  }

  .uploadContent {
    position: relative;
    width: 40vw;
    height: 360px;
    padding: 100px;
    border: 4px solid #000000;
    background-color: #ffffff;
    display: flex;
    flex-direction: column;
    justify-content: center;
    .inputBox {
      .input {
        display: none;
      }
    }

    .iconBox {
      display: flex;
      justify-content: center;
      //margin-top: 80px;

      img {
        width: 80px;
        height: 80px;
      }
    }

    .textBox {
      //margin-top: 85px;

      :nth-child(1) {
        color: #000000;
        font-size: 30px;
        font-weight: 600;
      }

      :nth-child(2) {
        color: #000000;
        font-size: 20px;
        font-weight: bold;
        letter-spacing: 2px;
      }
    }

  }

  .parserButton {
    margin-top: 80px;
    .button{
      transition: .2s;
      font-size: 22px;
      font-weight: bold;
      display: inline-block;
      padding: 10px 30px;
      background-color: #ffffff;
      border: 4px solid #000000;
      &::selection{
        background: transparent;
      }
      &:hover{
        user-select: none;
        cursor: pointer;
        background-color: #000000;
        color: #ffffff;
      }
    }
  }
}

</style>
<script>
export default {
  data() {
    return {
      msg: "模板语法"
    }
  }
}
</script>
