<template>
    <div id="app">
        <el-container>
            <el-header>欢迎访问百知教育管理系统</el-header>
            <el-container>
                <el-aside width="200px">
                    <router-link to="/user">用户管理</router-link>
                    <br>
                    <router-link to="/addr">地址管理</router-link>
                    <br>
                    <router-link to="/note">留言板</router-link>
                </el-aside>
                <el-main><router-view></router-view></el-main>
            </el-container>
        </el-container>
    </div>
</template>

<script>
import First from "./components/First";
import Second from "./components/Second";

export default {
    name: 'App',
    components: {
        first: First,
        second: Second,
    }
}
</script>

<style>
.el-header, .el-footer {
    background-color:pink;
    color: #333;
    text-align: center;
    line-height: 60px;
    font-size: 25px;
}

.el-aside {
    background-color:pink;
    color: #333;
    text-align: center;
    line-height: 160px;
}

.el-main {
    background-color: #E9EEF3;
    color: #333;
    line-height: 40px;
    text-align: center;
}

body > .el-container {
    margin-bottom: 10px;
}

.el-container:nth-child(5) .el-aside,
.el-container:nth-child(6) .el-aside {
    line-height: 20px;
}

.el-container:nth-child(7) .el-aside {
    line-height: 10px;
}
</style>
