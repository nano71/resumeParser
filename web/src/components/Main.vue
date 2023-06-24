<template>
  <div id="main">
    <div class="content" v-if="false">
      <div class="topTitle">
        渐进式简历解析系统
      </div>
<!--      未开始上传-->

      <div class="uploadContent">
      <div v-if="false">
        <div class="transformBox">
          <div v-for="item in 80" :key="item" class="transformItems"></div>
        </div>
        <div class="inputBox">
          <input class="input" type="file" accept=".doc,.docx,.pdf,.png,.jpg,.jpeg,.bmp,.txt"/>
        </div>
        <div class="iconBox">
          <img src="../assets/file.png" alt="">
        </div>
        <div class="textBox">
          <div>点击 或 拖拽</div>
          <div>即可上传简历文件</div>
        </div>
      </div >
        <div class="uploading">
          <div class="uploadingIcon"></div>
          <div class="uploadingText">文件: {{fileName}} 上传中</div>
          <div class="uploadingBar">
            <div class="current" :style="{width:current*100+'%'}"></div>
          </div>
        </div>
      </div>



        <div class="parserButton">
        <div class="button">开始解析</div>
<!--      上传完成-->
      </div>
    </div>
    <ResumeDetail/>
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
    width: 800px;
    height: 360px;
    padding: 100px;
    border: 4px solid #000000;
    background-color: #ffffff;
    display: flex;
    flex-direction: column;
    justify-content: center;
    overflow: hidden;
    //悬浮态
    &:hover .transformBox{
      opacity: 1;
      animation: 2s loops infinite linear;
    }
    .transformBox {
      opacity: 0;
      transform: translate(-50%, -50%) rotate(135deg);
      position: absolute;
      top: 50%;
      left: 50%;
      width: 150%;
      //height: 150%;

      @keyframes loops {
        0% {
          transform: translate(-50%, -50%) rotate(135deg);
        }

        100% {
          transform:translate(-39%, -39%) rotate(135deg);
        }

      }


      .transformItems {
        width: 100%;
        height: 20px;
        background-color: #ffffff;

        &:nth-child(even) {
          background-color: #000000;
          opacity: .05;
        }
      }

    }

    .inputBox {

      .input {
        cursor: pointer;

        position: absolute;
        z-index: 1;
        width: 100%;
        height: 100%;
        left: 0;
        top: 0;
        opacity: 0;
        //width: 100px;
        //height: 100px;
        //display: none;
      }
    }

    .iconBox {
      position: relative;
      display: flex;
      justify-content: center;
      //margin-top: 80px;

      img {
        width: 80px;
        height: 80px;
      }
    }

    .textBox {
      position: relative;
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

    .uploading{
      width: 100%;
      height: 100%;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      @keyframes loops2{
        0%{
          transform: rotate(0deg);
        }
        100%{
          transform: rotate(360deg);
        }
      }
      .uploadingIcon{
        width: 80px;
        height: 80px;
        border-radius:50% ;
        border:4px solid #00000010;
        border-top-color: black;
        animation: 1s loops2 infinite linear;
        margin-bottom: 20px;
      }
      .uploadingBar{
        width: 100%;
        height: 4px;
        background-color: #00000010;
        position: absolute;
        bottom: 0;
      .current{
        height: inherit;
        background-color: #000000;
      }
      }
    }
  }

  .parserButton {
    margin-top: 80px;
    display: flex;
    justify-content: center;

    .button {
      transition: .2s;
      font-size: 22px;
      font-weight: bold;
      padding: 10px 30px;
      background-color: #ffffff;
      border: 4px solid #000000;

      &::selection {
        background: transparent;
      }

      &:hover {
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
import ResumeDetail from "./resumeDetail.vue";
export default {
  components:{ResumeDetail},
  data() {
    return {
      current:0.1,
      msg: "模板语法",
      fileName:"untitled.pdf",
      personData:null
    }
  },
  created() {
    this.personData = {
      name:"唐斌",
      age:"22",
      phone:"13481323106",
      email:"2052089494@qq.com",
      highestEducation:"本科",
      school:"桂林理工大学"
    }
  }
}
</script>
