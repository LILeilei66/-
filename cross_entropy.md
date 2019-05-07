关于交叉熵，书上没有找到，参见csdn https://blog.csdn.net/tsyccnh/article/details/79163834

<h3> A. 背景知识:

1. 信息量：

   ```I(x) = -log(P(x))```
2. 信息量期望:

   利用熵来表示.
   
   ```H(x) = - sum{P(x_i) * log(P(x_i))}```
   
3. 相对熵(KL 散度)：

   (有分布 P, Q, 比较二者)
   
   ```D_KL(P||Q) = sum{P(x_i) * log(P(x_i)/Q(x_i))}```
   
4. 交叉熵：
   H(p, q) = - sum {p(x_i) * log(q(x_i))}
   产生原因:
       ```D_KL(p||q) = sum{p(x_i) * log(p(x_i)/q(x_i))}
       
                  = sum{p(x_i) * log(p(x_i))} - sum {p(x_i) * log(q(x_i))}
                  
                  = H(p) - sum {p(x_i) * log(q(x_i))}```
       <p = 真实分布 => H(p) 不变, 所以可以只看后者>
    e.g.:
      ```y_ = array([[0.18521222, 0.14295502, 0.6718327 ],
      
                  [0.15282199, 0.10026189, 0.7469162 ]], dtype=float32)
                  
      target = <tf.Tensor: id=90, shape=(2,), dtype=int32, numpy=array([1, 2])>
      
      H = - (1 * log(0.14295502) + 1 * log(0.7469162)) = -2.237027555704117```
      注：在 tf 以 mean 作为 loss.
