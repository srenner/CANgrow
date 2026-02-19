import { ref, onMounted } from 'vue';

export function useFahrenheit() {
    const isFahrenheit = ref(false);

    const toggleTemperatureUnit = () => {
        isFahrenheit.value = !isFahrenheit.value;
        if (isFahrenheit.value) {
            localStorage.setItem('temperatureUnit', 'f');
        } 
        else {
            localStorage.setItem('temperatureUnit', 'c');
        }
    };

    onMounted(() => {
        const savedTemperatureUnit = localStorage.getItem('temperatureUnit');
        if (savedTemperatureUnit === 'f') {
            isFahrenheit.value = true;
        }
        else {
            isFahrenheit.value = false;
        }
    });

    return { isFahrenheit, toggleTemperatureUnit };
}