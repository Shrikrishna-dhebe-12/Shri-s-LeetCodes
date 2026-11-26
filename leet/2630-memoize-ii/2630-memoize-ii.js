function memoize(fn) {
    const VALUE = Symbol();
    const root = new Map();

    return function (...args) {
        let node = root;

        for (const arg of args) {
            if (!node.has(arg)) node.set(arg, new Map());
            node = node.get(arg);
        }

        if (node.has(VALUE)) return node.get(VALUE);

        const res = fn(...args);
        node.set(VALUE, res);

        return res;
    };
}