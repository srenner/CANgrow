<script setup lang="ts">
    // get environment history

    /*
        id: int | None = Field(default=None, primary_key=True)
        environment_id: int | None = Field(default=None, foreign_key="environment.id")
        light_status: bool | None
        heat_status: bool | None
        temperature: float | None
        humidity: float | None
        gas: float | None
        datetime: int = Field(default=int(time.time()))
    */

    // use the history record datetime instead
    const now = new Date(1767408837 * 1000).toLocaleString();

</script>

<template>
    <div>
        light: on heat: off temp: 00.0 humid: 00.0 as of {{ now }}
    </div>
</template>

<style scoped>

</style>