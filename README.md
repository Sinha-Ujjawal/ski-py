## Implementation of simple datastructures using SK(I) Combinator Calculus

This repo contains simple datastructures implementation using [SK(I) Combinator Calculus](https://en.wikipedia.org/wiki/SKI_combinator_calculus). All the implementations are done in [Python 3.7+](https://www.python.org/downloads/release/python-370/)

## SK(I) Combinators

### S Combinator

```
S := \f g x. f x (g x)
```

### K Combinator

```
K := \x y. x
```

### I Combinator (Can be defined in terms of S & K)

```
I := \x. x
  := \x. K x K
  := \x. K x (K K x)
  := \x. S K (K K) x
  := S K (K K)
```

## References

1. (Book) [Purely Functional Data Structures - Okasaki](https://www.amazon.in/Purely-Functional-Structures-Chris-Okasaki/dp/0521663504)

2. (Youtube) [A Flock of Functions: Lambda Calculus and Combinatory Logic in JavaScript | Gabriel Lebec @ DevTalks](https://youtu.be/6BnVo7EHO_8)

## License & Copyright

Licensed under [@MIT](./LICENSE)
