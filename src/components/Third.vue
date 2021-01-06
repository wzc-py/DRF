<template>
    <div>
        <input type="text" v-model="msg">
        <input type="button" value="给他/她留言" @click="add_txt">
        <ul>
            <li v-for="(value,index) in note" :key="index">
                <span>{{ value }}</span>&nbsp;&nbsp;&nbsp;<a href="javascript:;" @click="del_note(index)">删除</a>
            </li>
        </ul>
        <span>总留言：{{ note.length }}条</span>
        <input type="button" value="清空留言" @click="del_all" v-show="note.length != 0">
    </div>
</template>

<script>
export default {
    name: "Third",
    data() {
        return {
            msg: "",
            note: localStorage.note ? JSON.parse(localStorage.note) : [],
        }
    },
    methods: {
        add_txt() {
            let msg = this.msg;
            if (msg) {
                this.note.push(this.msg);
                localStorage.note = JSON.stringify(this.note);
                this.msg = '';
            }
        },
        del_note(index) {
            this.note = JSON.parse(localStorage.note);
            this.note.splice(index, 1);
            localStorage.note = JSON.stringify(this.note);
        },
        del_all() {
            localStorage.clear();
        }
    },
}
</script>

<style scoped>

</style>
