void update_add(int l, int r, ll k) {

  l = P + l - 1;
  r = P + r + 1; // 哨兵位置
  int siz = 1;   // 记录当前子树大小

  while (l ^ 1 ^ r) { // 当l与r互为兄弟时，只有最后一位不同
    if (~l & 1)
      tr[l ^ 1] += siz * k, sum[l ^ 1] += k;
    if (r & 1)
      tr[r ^ 1] += siz * k, sum[r ^ 1] += k;
    // 类似递归线段树 tr[p] += tag[p]*(r-l+1)
    l >>= 1;
    r >>= 1;
    siz <<= 1;
    // 每次向上走时子树大小都会增加一倍
    tr[l] = tr[l << 1] + tr[l << 1 | 1] + sum[l] * siz; // 维护父子关系
    tr[r] = tr[r << 1] + tr[r << 1 | 1] + sum[r] * siz;
  }
  for (l >>= 1, siz <<= 1; l; l >>= 1, siz <<= 1)
    tr[l] = tr[l << 1] + tr[l << 1 | 1] + sum[l] * siz; // 更新上传至根节点
}

ll query_sum(int l, int r) {
  l = l + P - 1;
  r = r + P + 1;
  ll res = 0;
  int sizl = 0, sizr = 0, siz = 1; // 分别维护左右两侧子树大小

  while (l ^ 1 ^ r) {
    if (~l & 1)
      res += tr[l ^ 1], sizl += siz; // 更新答案及子树大小
    if (r & 1)
      res += tr[r ^ 1], sizr += siz;
    l >>= 1;
    r >>= 1;
    siz <<= 1;

    res += sum[l] * sizl + sum[r] * sizr;
    // 即使当前节点所存的区间和不需要用，但因为其是两个哨兵的父亲节点，且 tag
    // 不会下传， 所以其 tag 会对答案有贡献，所以需要加上 tag 的贡献
  }
  for (l >>= 1, sizl += sizr; l; l >>= 1)
    res += sum[l] * sizl; // 累加至根节点
  return res;
}