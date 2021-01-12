<template>
    <div>
        <el-container>
            <el-header>百知学员信息管理系统</el-header>
            <el-main><el-table :data="book_list" border style="width: 100%">
                <el-table-column  prop="id" label="id" width="120"></el-table-column>
                <el-table-column prop="book_name" label="书名" width="120"></el-table-column>
                <el-table-column prop="price" label="价格" width="120"></el-table-column>
                <el-table-column prop="pic" label="图片" width="120"></el-table-column>
                <el-table-column label="作者" width="180">
                    <template slot-scope="scope">
                        <el-popover trigger="hover" placement="top" v-for="(author,index) in scope.row.author_list" :key="index">
                            <p>作者: {{ author.author_name}}</p>
                            <p>年龄: {{ author.age }}</p>
                            <p>电话: {{ author.detail__phone }}</p>
                            <div slot="reference" class="name-wrapper">
                                <el-tag size="medium">{{ author.author_name }}</el-tag>
                            </div>
                        </el-popover>
                    </template>
                </el-table-column>
                <el-table-column prop="publish_name" label="出版社" width="120"></el-table-column>
                <el-table-column label="日期" width="180">
                    <template slot-scope="scope">
                        <i class="el-icon-time"></i>
                        <span style="margin-left: 10px">{{ scope.row.create_time }}</span>
                    </template>
                </el-table-column>
                <el-table-column prop="publish_address" label="出版社地址" width="120"></el-table-column>
            </el-table></el-main>
        </el-container>
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
        let id = this.$route.params.id;
        console.log(id);
        this.$axios({
            url:"http://127.0.0.1:8000/lastapp/book/",
            method:"get",
            params: {id:id},
        }).then(response=>{
            console.log(response.data);
            this.user_list = [response.data.results];
        }).catch(error=>{

        })
    }
}
</script>

<style scoped>

</style>
