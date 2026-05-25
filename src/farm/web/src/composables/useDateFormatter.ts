export function useDateFormatter() {
    const formatDate = (d:any) => {
        if(!d) return '';
        return new Date(d).toLocaleString();
    }
    return { formatDate };
}
