<template>
    <div>
        <el-table
            :data="user_list"
            border
            style="width: 100%">
            <el-table-column
                fixed
                prop="id"
                label="ID"
                width="150">
            </el-table-column>
            <el-table-column
                prop="username"
                label="姓名"
                width="120">
            </el-table-column>
            <el-table-column
                prop="age"
                label="年龄"
                width="120">
            </el-table-column>
            <el-table-column
                prop="salary"
                label="薪资"
                width="120">
            </el-table-column>
            <el-table-column
                prop="bir"
                label="日期"
                width="120">
            </el-table-column>
            <el-table-column
                prop="addr"
                label="地址"
                width="300">
            </el-table-column>
        </el-table>
    </div>
</template>

<script>
export default {
    name: "User_details",
    data(){
        return{
            user_list:[],
        }
    },
    created() {
        let id = this.$route.query.id;
        this.$axios({
            url:"http://127.0.0.1:8000/vuexapp/get_emp/",
            method:"get",
            params: {user_id:id},
        }).then(response=>{
            console.log(response.data);
            this.user_list = response.data;
        }).catch(error=>{

        })
    }
}
</script>

<style scoped>

</style>
