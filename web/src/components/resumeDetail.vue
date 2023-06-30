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
        <div :class="{navItem:1, select:i===isDetailInfo}" v-for="(item,i) in ['简历详情','分析数据']"
             @click="isDetailInfo=i">
          {{ item }}
        </div>
      </div>
    </div>
    <!--    第一页-->
    <div class="basicInform" v-if="!isDetailInfo">
      <div class="contentBox">
        <div class="title">
          <span>基本信息</span>
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
          <span>教育背景</span>
          <div class="titleMask"></div>
        </div>
        <div class="educationDetail">
          <div class="schoolName">
            <span class="name">桂林理工大学</span>
            <span class="time garyText">2019.09 - 至今</span>
          </div>
          <div class="educationItem">
            <div class="items" v-for="item in 6" :key="item">
              <span class="garyText">开始时间 : </span>
              <span>2019.09</span>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!--  第二页-->
    <div class="resultPage" v-else>
      <div class="brightPoit">
        <div class="title">
          <span>简历亮点</span>
          <div class="titleMask"></div>
        </div>
        <div class="highlightBox">
          <div class="highlightItem" v-for="item in 2" :key="item">
            <div class="itemTile">
              <div class="itemIcon">
                <img src="../assets/thumb_up.png" alt="">
              </div>
              <div class="itemTitleText">简历亮点 x 1</div>
            </div>
            <div class="itemText">
              <span>有丰富的前端开发经验，对vue、react、css、webpack、jquery、ajax、JavaScript、前端开发、node.js、bootstrap等技能或工具有深入的理解</span>
            </div>
          </div>
        </div>
      </div>
      <div class="personTag">
        <div class="tagContainer">
          <div class="title">
            <span>候选人标签</span>
            <div class="titleMask"></div>
          </div>
          <div class="tagListBox">
            <div class="tagList" v-for="item in 6" :key="item">
              <div class="tagTitle">基本标签</div>
              <div class="tagListItem">
                <div class="tagItem" v-for="(item,index) in 20" :key="index">22岁</div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="echartsBox">
        <div class="echartsItem"></div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "resumeDetail",
  data() {
    return {
      isDetailInfo: 1
    }
  }
}
</script>

<style lang="less" scoped>
#resumeDetail {
  margin-top: 80px;
  width: 800px;
  min-height: 99vh;
  border: 4px solid #000000;
  display: flex;
  flex-direction: column;
  row-gap: 40px;
  text-align: left;

  img {
    width: 100%;
    height: 100%;
  }

  .title {
    span {
      font-size: 22px;
      position: relative;
      text-align: left;
      width: auto;
      display: inline-block;

      &::after {
        content: '';
        display: block;
        width: 100%;
        height: 20px;
        background-color: #00000020;
        position: absolute;
        bottom: -5px;
        left: 20px;
      }
    }
  }

  .basicInform {
    display: flex;
    flex-direction: column;
    row-gap: 40px;
    padding: 0 40px;
  }

  .garyText {
    color: #00000080;
  }
}


.topBox {
  padding: 40px 40px 0;
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

      .name {
        font-weight: bold;
      }

      .time {
        font-size: 14px;
      }
    }

    .educationItem {
      display: flex;
      flex-direction: column;
      row-gap: 15px;
    }
  }
}

.resultPage {
  display: flex;
  flex-direction: column;
  row-gap: 40px;
  padding: 0 40px;

  .highlightBox {
    display: flex;
    flex-direction: column;
    row-gap: 20px;
    padding: 40px 5px 0;
    text-align: left;

    .highlightItem {
      display: flex;
      flex-direction: column;
      row-gap: 10px;

      .itemTile {
        display: flex;
        column-gap: 10px;
        //justify-content: center;
        align-items: center;

        .itemIcon {
          width: 14px;
          height: 14px;

          img {
            position: relative;
            top: -3px;
          }
        }

      }

      .itemText {
        font-size: 14px;
        color: #00000080;
      }

    }
  }

  .personTag {
    .tagContainer {
      .tagListBox {
        padding-top: 40px;
        display: flex;
        flex-direction: column;
        row-gap: 15px;

        .tagList {
          display: flex;
          flex-direction: column;
          row-gap: 15px;

          .tagListItem {
            display: flex;
            flex-wrap: wrap;
            gap: 15px;

            .tagItem {
              padding: 4px 10px;
              background-color: #00000080;
              color: #ffffff;
            }
          }
        }
      }
    }
  }

  .echartsBox {
    display: flex;
    flex-direction: column;
    row-gap: 40px;
  }
}
</style>
