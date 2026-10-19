-- Numbered display equations: $$ ... \tag{n} $$  ->  borderless 1x2 table
-- (display math centred in the left cell, "(n)" right-aligned in the right cell).
-- Horizontal rules (---) are dropped.
local function eq_table(tex, num)
  local pad = pandoc.Cell({}, "AlignLeft")
  local mid = pandoc.Cell({pandoc.Para({pandoc.Math("DisplayMath", tex)})}, "AlignCenter")
  local right = pandoc.Cell({pandoc.Para({pandoc.Str("(" .. num .. ")")})}, "AlignRight")
  local body = {attr = pandoc.Attr(), body = {pandoc.Row({pad, mid, right})}, head = {}, row_head_columns = 0}
  return pandoc.Table({long = {}, short = nil}, {{"AlignLeft", 0.1}, {"AlignCenter", 0.8}, {"AlignRight", 0.1}},
    pandoc.TableHead(), {body}, pandoc.TableFoot(), pandoc.Attr("", {"eqtable"}))
end

function Para(el)
  if #el.content == 1 and el.content[1].t == "Math" and el.content[1].mathtype == "DisplayMath" then
    local tex = el.content[1].text
    local body, num = tex:match("^(.-)%s*\\tag{([^}]*)}%s*$")
    if num then return eq_table(body, num) end
  end
end

function HorizontalRule() return {} end
