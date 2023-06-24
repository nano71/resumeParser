<template>
  <div id="resumeDetail">
    <div class="topBox">
      <div class="personDetail">
        <div class="headImg"></div>
        <div class="detailCard">
          <div class="top">
            <span class="name">唐斌</span>
            <span class="label">技术达标</span>
          </div>
          <div class="bottom">
            <div class="item">
              <div class="icon"></div>
              <div class="text">22岁</div>
            </div>
          </div>
        </div>
      </div>
      <div class="navBar">
        <div class="navItem select">简历详情</div>
        <div class="navItem">分析数据</div>
      </div>
    </div>
    <div class="contentBox">
      <div class="title">
        <sapn>基本信息</sapn>
        <div class="titleMask"></div>
      </div>
      <div class="messageDetails">
        <div class="messageItem" v-for="item in 6" :key="item">
          <div class="doll"></div>
          <div class="items">
            <span class="garyText">
              姓名 :
            </span>
            <span>唐斌</span>
          </div>
        </div>
      </div>
    </div>
    <div class="contentBox">
      <div class="title">
        <sapn>教育背景</sapn>
        <div class="titleMask"></div>
      </div>
      <div class="educationDetail">
        <div class="schoolName">
          <span class="name">桂林理工大学</span>
          <span class="time garyText">2019.09 - 至今</span>
        </div>
        <div class="educationItem">
          <div class="items" v-for="item in 6">
            <span class="garyText">开始时间 : </span>
            <span>2019.09</span>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
export default {
  name: "resumeDetail"
}
</script>

<style lang="less" scoped>
#resumeDetail {
  width: 800px;
  min-height: 99vh;
  border: 4px solid #000000;
  display: flex;
  flex-direction: column;
  row-gap: 40px;
  padding: 0 20px;
}

.garyText {
  color: #00000080;
}

.topBox {
  padding: 20px 20px 0 20px;
  border-bottom: 1px solid #00000040;

  .personDetail {
    display: flex;

    .headImg {
      width: 60px;
      height: 70px;
      background-color: #000000;
      margin-right: 20px;
    }

    .detailCard {
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      padding-bottom: 10px;

      .top {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 10px;

        .name {
          font-size: 22px;
          font-weight: bold;
          margin-right: 20px;

        }

        .label {
          width: auto;
          padding: 0 6px;
          font-size: 12px;
          height: 20px;
          display: flex;
          justify-content: center;
          align-items: center;
          background-color: #00000020;
          color: #000000;
        }

      }

      .bottom {
        display: flex;

        .item {
          margin-right: 10px;
          display: flex;

          .icon {
            width: 15px;
            height: 15px;
            background-color: #00000020;
            margin-right: 5px;
          }

          .text {
            font-size: 12px;
            color: #00000060;
          }
        }
      }
    }
  }

  .navBar {
    margin-top: 20px;
    display: flex;
    position: relative;
    top: 2px;

    .navItem {
      color: #00000060;
      width: 80px;
      height: 40px;
      display: flex;
      justify-content: center;
      align-items: center;
      margin-right: 40px;
      cursor: pointer;

      &.select {
        color: #000000;
        border-bottom: 4px solid #000000;
      }
    }

  }
}

.contentBox {

  .title {
    font-size: 22px;
    position: relative;
    text-align: left;

    .titleMask {
      width: 90px;
      height: 20px;
      background-color: #00000020;
      position: absolute;
      bottom: -5px;
      left: 20px;
    }
  }

  .messageDetails {
    box-sizing: border-box;
    width: 100%;
    padding: 40px 5px 0 5px;
    display: flex;
    flex-wrap: wrap;
    row-gap: 15px;

    .messageItem {
      box-sizing: border-box;
      flex: 0 0 50%;
      text-align: left;
      display: flex;
      //justify-content: center;
      align-items: center;

      .doll {
        width: 5px;
        height: 5px;
        background-color: #000000;
        margin-right: 10px;
      }


    }
  }

  .educationDetail {
    margin-top: 40px;
    text-align: left;

    .schoolName {

      margin-bottom: 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      .name{
        font-weight: bold;
      }
      .time{
        font-size: 14px;
      }
    }
  .educationItem{
    display: flex;
    flex-direction: column;
    row-gap: 15px;
  }
  }
}

</style>
