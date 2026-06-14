import { ref, computed, type Ref } from 'vue';

/**
 * Holds an array of T
 * 
 * @param getValue 
 * @param getTimestamp 
 * @param windowMs 
 * @returns 
 */
export function useLiveCache<T>(
    getValue: (item: T) => number,
    getTimestamp: (item: T) => number,
    windowMs = 15 * 60 * 1000
){
    const queue = ref<T[]>([]) as Ref<T[]>;

    /** Returns UNIX timestamp of oldest value acceptable */
    function cutoff(): number {
        return Date.now() - windowMs;
    }

    function add(item: T) {
        if(getTimestamp(item) < cutoff()) return;
        const itemTimestamp = getTimestamp(item);

        let index = queue.value.length - 1;
        while(index >= 0 && getTimestamp(queue.value[index]!) > itemTimestamp) index--;
        queue.value.splice(index + 1, 0, item);
    }

    const items = computed(() => {
          return queue.value.filter((item) => getTimestamp(item) >= cutoff())
    });

    function prune() {
        const c = cutoff();
        const firstValid = queue.value.findIndex((item) => getTimestamp(item) >= c);
        if(firstValid === -1) queue.value = [];
        else if (firstValid > 0) queue.value.splice(0, firstValid);
    }

    function clear() {
        queue.value = [];
    }

    return { add, items, prune, clear };
}
