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
                width="150">
            </el-table-column>
            <el-table-column
                fixed="right"
                label="操作"
                width="200">
                <template slot-scope="scope">
                    <el-button @click="handleClick(scope.row.id)" type="text" size="small">查看</el-button>
                    <el-button @click="add_emp()" type="text" size="small">添加</el-button>
                    <!--                <el-button @click="check_emp(scope.row.id)" type="text" size="small">修改</el-button>-->
                    <el-button @click="del_user(scope.row.id)" type="text" size="small">删除</el-button>
                </template>
            </el-table-column>
        </el-table>
    </div>
</template>

<script>
export default {
    name: "First",
    methods: {
        //查看员工
        handleClick(row) {
            this.$router.push("/user_de?id=" + row)
        },
        //删除员工
        del_user(row) {
            this.$axios({
                url: "http://127.0.0.1:8000/vuexapp/del_emp/",
                method: "get",
                params: {id: row},
            }).then(response => {
                this.user_list = response.data;
            }).catch(error => {

            })
        },
        //增加员工
        add_emp() {
            this.$router.push("/add_emp")
        },
    },

        data() {
            return {
                user_list:[],
            }
        },

        created() {
            this.$axios({
                url: "http://127.0.0.1:8000/vuexapp/emp/",
                method: "get",
            }).then(response => {
                console.log(response.data);
                this.user_list = response.data;
            }).catch(error => {

            })
        }
    }

</script>

<style scoped>

</style>
