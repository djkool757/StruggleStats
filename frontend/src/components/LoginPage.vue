 <script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';


const username = ref('');
const password = ref('');

function handleLogin() {
    //make an API call to authenticate the user
    
    console.log('Logging in with', username.value, password.value);
    // Redirect to the home page after login
    const router = useRouter();
    router.push('/');
}
</script>

<template>
    <div class="login-page">
        <h1>Login Page</h1>
        <form @submit.prevent="handleLogin">
        <div>
            <label for="username">Username:</label>
            <input type="text" id="username" v-model="username" required />
        </div>
        <div>
            <label for="password">Password:</label>
            <input type="password" id="password" v-model="password" required />
        </div>
        <button type="submit">Login</button>
        </form>
    </div>
</template>

<style scoped>

</style>