#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
红黑树 (Red-Black Tree) 的 Python 实现

红黑树是一种自平衡二叉查找树，具有以下性质：
1. 每个节点要么是红色，要么是黑色
2. 根节点是黑色
3. 每个叶子节点（NIL节点）是黑色
4. 如果一个节点是红色，则它的两个子节点都是黑色（不能有连续的红节点）
5. 从任一节点到其每个叶子的所有路径都包含相同数目的黑色节点

核心操作：
- 插入：O(log n)
- 搜索：O(log n)
- 旋转和重新着色以维持平衡
"""

from enum import Enum
from typing import Optional, Any, List


class Color(Enum):
    RED = True
    BLACK = False


class Node:
    """红黑树节点"""
    
    def __init__(self, key: Any, value: Any = None, color: Color = Color.RED):
        self.key = key
        self.value = value
        self.color = color
        self.left: Optional['Node'] = None
        self.right: Optional['Node'] = None
        self.parent: Optional['Node'] = None
    
    def is_red(self) -> bool:
        """判断节点是否为红色"""
        return self.color == Color.RED
    
    def is_black(self) -> bool:
        """判断节点是否为黑色"""
        return self.color == Color.BLACK
    
    def __repr__(self):
        color_str = "R" if self.is_red() else "B"
        return f"Node({self.key}, {color_str})"


class RedBlackTree:
    """红黑树实现"""
    
    def __init__(self):
        self.nil = Node(None, None, Color.BLACK)  # NIL 节点（哨兵）
        self.root: Optional[Node] = self.nil
    
    def insert(self, key: Any, value: Any = None) -> None:
        """插入新节点"""
        new_node = Node(key, value, Color.RED)
        new_node.left = self.nil
        new_node.right = self.nil
        
        parent = None
        current = self.root
        
        # 标准 BST 插入
        while current != self.nil:
            parent = current
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                # 键已存在，更新值
                current.value = value
                return
        
        new_node.parent = parent
        
        if parent is None:
            self.root = new_node
        elif key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node
        
        # 修复红黑树性质
        self._fix_insert(new_node)
    
    def _fix_insert(self, node: Node) -> None:
        """修复插入后可能破坏的红黑树性质"""
        while node != self.root and node.parent.is_red():
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                
                if uncle.is_red():
                    # Case 1: 叔父节点为红色 - 重新着色
                    node.parent.color = Color.BLACK
                    uncle.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        # Case 2: 当前节点是右孩子 - 左旋
                        node = node.parent
                        self._left_rotate(node)
                    
                    # Case 3: 当前节点是左孩子 - 右旋 + 重新着色
                    node.parent.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    self._right_rotate(node.parent.parent)
            else:
                # 对称情况（父节点是祖父节点的右孩子）
                uncle = node.parent.parent.left
                
                if uncle.is_red():
                    # Case 1: 叔父节点为红色 - 重新着色
                    node.parent.color = Color.BLACK
                    uncle.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        # Case 2: 当前节点是左孩子 - 右旋
                        node = node.parent
                        self._right_rotate(node)
                    
                    # Case 3: 当前节点是右孩子 - 左旋 + 重新着色
                    node.parent.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    self._left_rotate(node.parent.parent)
        
        # 根节点必须为黑色
        self.root.color = Color.BLACK
    
    def _left_rotate(self, node: Node) -> None:
        """左旋操作"""
        right_child = node.right
        node.right = right_child.left
        
        if right_child.left != self.nil:
            right_child.left.parent = node
        
        right_child.parent = node.parent
        
        if node.parent is None:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child
        
        right_child.left = node
        node.parent = right_child
    
    def _right_rotate(self, node: Node) -> None:
        """右旋操作"""
        left_child = node.left
        node.left = left_child.right
        
        if left_child.right != self.nil:
            left_child.right.parent = node
        
        left_child.parent = node.parent
        
        if node.parent is None:
            self.root = left_child
        elif node == node.parent.right:
            node.parent.right = left_child
        else:
            node.parent.left = left_child
        
        left_child.right = node
        node.parent = left_child
    
    def search(self, key: Any) -> Optional[Node]:
        """搜索指定键的节点"""
        current = self.root
        
        while current != self.nil:
            if key == current.key:
                return current
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        
        return None
    
    def inorder_traversal(self) -> List[tuple]:
        """中序遍历，返回 (key, value, color) 列表"""
        result = []
        self._inorder_helper(self.root, result)
        return result
    
    def _inorder_helper(self, node: Node, result: List[tuple]) -> None:
        """中序遍历辅助函数"""
        if node != self.nil:
            self._inorder_helper(node.left, result)
            color_str = "RED" if node.is_red() else "BLACK"
            result.append((node.key, node.value, color_str))
            self._inorder_helper(node.right, result)
    
    def print_tree(self) -> None:
        """打印树结构（中序遍历）"""
        items = self.inorder_traversal()
        if not items:
            print("树为空")
            return
        
        print("中序遍历结果 (Key, Value, Color):")
        for key, value, color in items:
            print(f"  ({key}, {value}, {color})")
    
    def is_empty(self) -> bool:
        """判断树是否为空"""
        return self.root == self.nil


def main():
    """测试红黑树"""
    print("=== 红黑树 Python 实现 ===\n")
    
    # 创建红黑树
    rb_tree = RedBlackTree()
    
    # 插入测试数据
    test_data = [
        (10, "Ten"),
        (20, "Twenty"),
        (30, "Thirty"),
        (15, "Fifteen"),
        (25, "Twenty-Five"),
        (5, "Five"),
        (1, "One"),
        (35, "Thirty-Five"),
        (28, "Twenty-Eight")
    ]
    
    print("插入数据:")
    for key, value in test_data:
        rb_tree.insert(key, value)
        print(f"  插入: ({key}, {value})")
    
    print("\n" + "="*40)
    rb_tree.print_tree()
    
    # 搜索测试
    print("\n" + "="*40)
    print("搜索测试:")
    search_keys = [15, 100, 5]
    
    for key in search_keys:
        node = rb_tree.search(key)
        if node:
            color = "RED" if node.is_red() else "BLACK"
            print(f"  找到键 {key}: 值={node.value}, 颜色={color}")
        else:
            print(f"  键 {key} 不存在")
    
    # 验证红黑树性质（简单检查）
    print("\n" + "="*40)
    print("红黑树性质验证:")
    print(f"  根节点颜色: {'BLACK' if rb_tree.root.is_black() else 'RED'} (应为 BLACK)")
    print(f"  树是否为空: {rb_tree.is_empty()}")
    
    # 统计节点数
    items = rb_tree.inorder_traversal()
    red_count = sum(1 for _, _, color in items if color == "RED")
    black_count = sum(1 for _, _, color in items if color == "BLACK")
    print(f"  总节点数: {len(items)}")
    print(f"  红色节点数: {red_count}")
    print(f"  黑色节点数: {black_count}")


if __name__ == "__main__":
    main()
