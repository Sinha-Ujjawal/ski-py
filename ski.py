# S := \f g x. f x (g x)
S = lambda f: lambda g: lambda x: f(x)(g(x))

# K := \x y. x
K = lambda x: lambda y: x

# I := \x. x
#   := \x. K x K
#   := \x. K x (K K x)
#   := \x. S K (K K) x
#   := S K (K K)
I = S(K)(K(K))

# KI := \x y. y
#    := \x y. I y
#    := \x. I
#    := \x. K I x
#    := K I
KI = K(I)

# B := \f g x. f (g x)
#   := \f g x. K f x (g x)
#   := \f g x. S (K f) g x
#   := \f. S (K f)
#   := \f. K S f (K f)
#   := \f. S (K S) K f
#   := S (K S) K
B = S(K(S))(K)

# T := \x f. f x
#   := \x f. I f x
#   := \x f. I f (K x f)
#   := \x f. S I (K x) f
#   := \x. S I (K x)
#   := \x. B (S I) K x
#   := B (S I) K
T = B(S(I))(K)

# V := \x y f. f x y
#   := \x y f. T x f y
#   := \x y f. T x f (K y f)
#   := \x y f. S (T x) (K y) f
#   := \x y. S (T x) (K y)
#   := \x y. B S T x (K y)
#   := \x y. B (B S T x) K y
#   := \x. B (B S T x) K
#   := \x. B B (B S T) x K
#   := \x. B B (B S T) x (K K x)
#   := \x. S (B B (B S T)) (K K) x
#   := S (B B (B S T)) (K K)
V = S(B(B)(B(S)(T)))(K(K))
