export function useDateFormatter() {
    const formatDate = (d:any) => {
        if(!d) return '';
        return new Date(d * 1000).toLocaleString();
    }
    return { formatDate };
}
